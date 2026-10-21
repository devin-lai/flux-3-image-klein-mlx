"""Packed transformer and Qwen text features using native MLX Metal operations."""
from __future__ import annotations

import gc
import json
import math
import os
from pathlib import Path
import struct

import mlx.core as mx
import mlx.nn as nn
import numpy as np

from .fast_kernels import qkv_rms_rope, attention_mlp_pack
from .compact_kernels import normalized as compact_normalized, residual as compact_residual


def validate_precision(precision):
    if precision not in ("legacy", "balanced", "scaled", "fp32"):
        raise ValueError(f"Unknown arithmetic precision: {precision}")
    if precision == "fp32" and os.environ.get("MLX_ENABLE_TF32") != "0":
        raise ValueError("Full FP32 requires MLX_ENABLE_TF32=0 before importing MLX; use the CLI --precision fp32")


def release():
    gc.collect()
    mx.synchronize()
    mx.clear_cache()


def load_component(path, *, cache_scaled_weights=False):
    weights = {}
    for shard in sorted(Path(path).glob("*.safetensors")):
        values = mx.load(str(shard))
        if cache_scaled_weights:
            # These matrices are already cast to FP16 by every scaled GEMM.
            # Cast once per shard and release the BF16 load buffer immediately.
            values = {k: v.astype(mx.float16) if v.dtype == mx.bfloat16 and v.ndim == 2
                      and k.endswith(".weight") and not k.startswith(("time_in.", "ref_time_in.",
                      "early_stream_modulations.", "single_stream_modulations.", "final_layer.")) else v
                      for k, v in values.items()}
        mx.eval(values)
        weights.update(values)
    return weights


def load_embedding_rows(path, ids):
    """Read only requested vocabulary rows; never copy the whole embedding."""
    with Path(path).open("rb") as f:
        length = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(length))
    dtypes = {"U32": np.uint32, "BF16": np.uint16, "F16": np.float16, "F32": np.float32}
    values = {}
    for key, spec in header.items():
        if key == "__metadata__":
            continue
        mapped = np.memmap(path, mode="r", dtype=dtypes[spec["dtype"]],
                           offset=8 + length + spec["data_offsets"][0], shape=tuple(spec["shape"]))
        value = mx.array(np.asarray(mapped[np.asarray(ids, dtype=np.int64)]))
        if spec["dtype"] == "BF16":
            value = value.view(mx.bfloat16)
        values[key] = value
        del mapped
    mx.eval(values)
    return values


class Weights:
    def __init__(self, weights, bits=16, group_size=64, *, quantization_map=None, matmul="quantized", precision="legacy"):
        validate_precision(precision)
        self.w, self.bits, self.group_size = weights, bits, group_size
        self.quantization_map = quantization_map or {}
        self.matmul = matmul
        self.precision = precision

    def spec(self, name):
        spec = self.quantization_map.get(name + ".weight", {})
        return spec.get("bits", self.bits), spec.get("group_size", self.group_size)

    def mode(self, name):
        """affine (scale and offset) unless the manifest names an MX/NV floating-point format."""
        return self.quantization_map.get(name + ".weight", {}).get("mode", "affine")

    def linear(self, name, x, *, scaled_input=False, scaled_output=False):
        w = self.w[name + ".weight"]
        scaled = self.precision == "scaled" and not name.startswith(("time_in.", "ref_time_in.",
                 "early_stream_modulations.", "single_stream_modulations.", "final_layer."))
        if scaled and not scaled_input:
            # Keep the residual stream and nonlinear products in FP32. Scale
            # only the GEMM operand, avoiding FP16 activation overflow.
            x = (x.astype(mx.float32) / 256).astype(mx.float16)
        if name + ".scales" in self.w and self.mode(name) != "affine":
            bits, group_size = self.spec(name)
            result = mx.quantized_matmul(x, w, self.w[name + ".scales"], None, group_size=group_size, bits=bits,
                                         mode=self.mode(name))
        elif name + ".scales" in self.w:
            bits, group_size = self.spec(name)
            scale = self.w[name + ".scales"].astype(x.dtype)
            bias = self.w[name + ".biases"].astype(x.dtype)
            if self.matmul == "dequantize":
                dense = mx.dequantize(w, scale, bias, group_size=group_size, bits=bits)
                result = x @ dense.T
            else:
                result = mx.quantized_matmul(x, w, scale, bias, group_size=group_size, bits=bits)
        else:
            result = x @ w.astype(x.dtype).T
        return result.astype(mx.float32) * 256 if scaled and not scaled_output else result

    def embedding(self, ids):
        w = self.w["embed_tokens.weight"][ids]
        if "embed_tokens.scales" in self.w:
            bits, group_size = self.spec("embed_tokens")
            w = mx.dequantize(w, self.w["embed_tokens.scales"][ids], self.w["embed_tokens.biases"][ids],
                              group_size=group_size, bits=bits)
        return w


@mx.compile
def modulate(x, scale, shift):
    return (1 + scale) * mx.fast.layer_norm(x, None, None, 1e-6) + shift


@mx.compile
def rms_rope(x, weight, cos, sin):
    normalized = mx.fast.rms_norm(x.astype(mx.float32), weight.astype(mx.float32), 1e-6)
    even, odd = normalized[..., 0::2], normalized[..., 1::2]
    return mx.stack([even * cos - odd * sin, even * sin + odd * cos], axis=-1).reshape(x.shape).astype(x.dtype)


def rotary(ids):
    # Match the official float64 construction, then use compact FP32 sin/cos.
    ids = np.asarray(ids, dtype=np.float64)
    angles = np.concatenate([ids[:, axis, None] / (10000 ** (np.arange(0, 32, 2) / 32))
                             for axis in range(4)], axis=-1)
    return mx.array(np.cos(angles).astype(np.float32))[None, None], mx.array(np.sin(angles).astype(np.float32))[None, None]


class Block:
    def __init__(self, weights, prefix, *, fused=False, precision="legacy"):
        # Explicit captured inputs prevent compilation from retaining a dense
        # dequantized copy of every matrix in the model.
        self.weights = Weights({k: v for k, v in weights.w.items() if k.startswith(prefix + ".")},
                               weights.bits, weights.group_size,
                               quantization_map=weights.quantization_map, matmul=weights.matmul, precision=precision)
        self.prefix, self.fused, self.precision = prefix, bool(fused), precision
        self.compact = fused == "fast" and precision == "scaled"
        self.forward = mx.compile(self._forward, inputs=self.weights.w)

    def _forward(self, x, cos, sin, shift, scale, gate, mode=None):
        w, p = self.weights, self.prefix
        normalized = compact_normalized(x, shift, scale, mode) if self.compact else modulate(x, scale, shift)
        if self.precision == "balanced":
            normalized = normalized.astype(mx.bfloat16)
        split_weights = p + ".qkv_proj.weight" in w.w
        compact_scaled = self.precision == "scaled" and self.fused
        if split_weights:
            projected = mx.concatenate([w.linear(p + ".qkv_proj", normalized, scaled_input=self.compact, scaled_output=compact_scaled),
                                         w.linear(p + ".mlp_in", normalized, scaled_input=self.compact, scaled_output=compact_scaled)], axis=-1)
        else:
            projected = w.linear(p + ".in_proj", normalized, scaled_input=self.compact, scaled_output=compact_scaled)
        if self.fused:
            q, k, v = qkv_rms_rope(projected, w.w[p + ".norm.query_norm.scale"],
                                  w.w[p + ".norm.key_norm.scale"], cos, sin,
                                  output_dtype=mx.float16 if self.precision == "scaled" else None,
                                  input_scale=256 if compact_scaled else 1)
            mlp = projected[:, 9216:]
        else:
            q, k, v, mlp = mx.split(projected, [3072, 6144, 9216], axis=-1)
            split = lambda t: t.reshape(1, -1, 24, 128).transpose(0, 2, 1, 3)
            q = rms_rope(split(q), w.w[p + ".norm.query_norm.scale"], cos, sin)
            k = rms_rope(split(k), w.w[p + ".norm.key_norm.scale"], cos, sin)
            v = split(v)
            if self.precision == "scaled":
                q, k, v = q.astype(mx.float16), k.astype(mx.float16), v.astype(mx.float16)
        attention = mx.fast.scaled_dot_product_attention(q, k, v, scale=128**-0.5)
        if self.fused:
            packed = attention_mlp_pack(attention, projected, precise=self.precision != "legacy",
                                        input_scale=256 if compact_scaled else 1,
                                        output_divisor=256 if compact_scaled else 1)
        else:
            attention = attention.transpose(0, 2, 1, 3).reshape(-1, 3072)
            gate_in, up = mx.split(mlp, 2, axis=-1)
            if self.precision != "legacy":
                mlp_output = (nn.silu(gate_in.astype(mx.float32)) * up.astype(mx.float32)).astype(projected.dtype)
            else:
                mlp_output = nn.silu(gate_in) * up
            packed = mx.concatenate([attention, mlp_output], axis=-1)
        if split_weights:
            output = w.linear(p + ".attn_out", packed[:, :3072], scaled_input=compact_scaled) + w.linear(p + ".mlp_out", packed[:, 3072:], scaled_input=compact_scaled)
            if self.compact:
                # The two projections have already restored the FP32 scale.
                return x + gate[mode] * output
        else:
            output = w.linear(p + ".out_proj", packed, scaled_input=compact_scaled, scaled_output=self.compact)
        if self.compact:
            return compact_residual(x, output, gate, mode)
        return x + gate * (output.astype(mx.float32) if self.precision != "legacy" else output)

    def __call__(self, x, freqs, mod, mode=None):
        return self.forward(x, *freqs, *mod, mode)


def timestep(t, dtype=mx.bfloat16):
    t = (mx.array([float(t)], dtype=dtype) * 1000).astype(mx.float32)
    freq = mx.exp(-math.log(10000) * mx.arange(128, dtype=mx.float32) / 128)
    args = t[:, None] * freq[None]
    return mx.concatenate([mx.cos(args), mx.sin(args)], axis=-1).astype(dtype)


class DiT:
    def __init__(self, model_dir, references=False, *, dtype=mx.bfloat16, matmul="quantized", fused=False, precision="legacy"):
        validate_precision(precision)
        manifest = json.loads((Path(model_dir) / "manifest.json").read_text())
        values = load_component(Path(model_dir) / "transformer", cache_scaled_weights=precision == "scaled")
        if references:
            values.update(load_component(Path(model_dir) / "image_conditioning", cache_scaled_weights=precision == "scaled"))
        self.weights = Weights(values, manifest["bits"], manifest["group_size"],
                               quantization_map=manifest.get("quantization_map"), matmul=matmul, precision=precision)
        self.precision = precision
        self.compact = fused == "fast" and precision == "scaled"
        self.dtype = mx.float32 if precision in ("fp32", "scaled") else dtype
        self.projected_text = self.projected_reference = None
        modes = ("image", "image_cond", "text") if references else ("image", "text")
        self.early = {m: [Block(self.weights, ("txt_mode_blocks" if m == "text" else "content_mode_blocks." + m)
                                    + f".{i}", fused=fused, precision=precision) for i in range(5)] for m in modes}
        self.single = [Block(self.weights, f"single_blocks.{i}", fused=fused, precision=precision) for i in range(28)]

    def prepare(self, schedule, ids):
        w = self.weights
        cond_dtype = mx.bfloat16 if self.precision == "legacy" else mx.float32
        embed = lambda prefix, t: w.linear(prefix + ".out_layer", nn.silu(w.linear(prefix + ".in_layer", timestep(t, cond_dtype))))
        self.mods = []
        fixed = embed("time_in", 0.)
        mx.eval(fixed)
        for index in range(len(schedule) - 1):
            ref = embed("ref_time_in", schedule[index + 1])
            vec = {m: (embed("time_in", schedule[index]) if m == "image" else fixed) + ref for m in ids}
            early, single = {}, {}
            for mode in ids:
                key = "txt" if mode == "text" else mode
                early[mode] = tuple(mx.split(w.linear("early_stream_modulations." + key + ".lin", nn.silu(vec[mode])), 3, axis=-1))
                single[mode] = tuple(mx.split(w.linear("single_stream_modulations." + key + ".lin", nn.silu(vec[mode])), 3, axis=-1))
            final = tuple(mx.split(w.linear("final_layer.image.adaLN_modulation.1", nn.silu(vec["image"])), 2, axis=-1))
            self.mods.append((early, single, final))
            # Do not retain FP32 weight-cast graphs for every timestep.
            mx.eval(self.mods[-1])
        if self.dtype != mx.bfloat16 and self.precision == "legacy":
            self.mods = [({m: tuple(a.astype(self.dtype) for a in v) for m, v in e.items()},
                          {m: tuple(a.astype(self.dtype) for a in v) for m, v in s.items()},
                          tuple(a.astype(self.dtype) for a in f)) for e, s, f in self.mods]
        mx.eval(self.mods)
        for key in list(w.w):
            if key.startswith(("time_in.", "ref_time_in.", "early_stream_modulations.",
                               "single_stream_modulations.", "final_layer.image.adaLN_modulation.")):
                del w.w[key]
        self.freqs = {m: rotary(i) for m, i in ids.items()}
        self.freqs["single"] = rotary(np.concatenate(list(ids.values()), axis=0))
        self.sizes = {m: len(i) for m, i in ids.items()}
        if self.compact:
            self.mode_index = {m: mx.zeros((len(i),), dtype=mx.int32) for m, i in ids.items()}
            self.mode_index["single"] = mx.concatenate(
                [mx.full((len(i),), n, dtype=mx.int32) for n, i in enumerate(ids.values())])
            mx.eval(self.mode_index)
        release()

    def __call__(self, image, text, reference, step):
        w = self.weights
        early, single, final = self.mods[step]
        x = {"image": w.linear("emb_in.image", image.astype(self.dtype))}
        if reference is not None:
            if self.projected_reference is None:
                self.projected_reference = w.linear("emb_in.image_cond", reference.astype(self.dtype))
                mx.eval(self.projected_reference)
            x["image_cond"] = self.projected_reference
        if self.projected_text is None:
            self.projected_text = w.linear("txt_in", text.astype(self.dtype))
            mx.eval(self.projected_text)
        x["text"] = self.projected_text
        if self.precision != "legacy":
            x = {m: value.astype(mx.float32) for m, value in x.items()}
        for layer in range(5):
            for mode in x:
                x[mode] = self.early[mode][layer](x[mode], self.freqs[mode], early[mode],
                                                self.mode_index[mode] if self.compact else None)
        h = mx.concatenate(list(x.values()), axis=0)
        mods = tuple(mx.concatenate([single[m][i] if self.compact else
                                     mx.broadcast_to(single[m][i], (self.sizes[m], 3072)) for m in x], axis=0)
                     for i in range(3))
        for block in self.single:
            h = block(h, self.freqs["single"], mods, self.mode_index["single"] if self.compact else None)
        shift, scale = final
        return w.linear("final_layer.image.linear", modulate(h[:self.sizes["image"]], scale, shift))


@mx.compile
def text_norm(x, weight):
    # Transformers rounds the normalized activation before multiplying weight.
    norm = mx.fast.rms_norm(x.astype(mx.float32), None, 1e-6).astype(x.dtype)
    return norm * weight


@mx.compile
def text_rope(x, cos, sin):
    half = x.shape[-1] // 2
    rotated = mx.concatenate([-x[..., half:], x[..., :half]], axis=-1)
    return x * cos + rotated * sin


class TextEncoder:
    def __init__(self, model_dir, *, streaming=False, precision="legacy"):
        validate_precision(precision)
        self.model_dir, self.streaming = Path(model_dir), streaming
        self.precision = precision
        self.dtype = mx.bfloat16 if precision == "legacy" else mx.float32
        manifest = json.loads((self.model_dir / "manifest.json").read_text())
        self.spec = dict(bits=manifest["bits"], group_size=manifest["group_size"],
                         quantization_map=manifest.get("quantization_map"), precision=precision)
        self.weights = None if streaming else Weights(load_component(self.model_dir / "text_encoder"), **self.spec)
        self.layer = [mx.compile(lambda x, cos, sin, mask, index=index: self._layer(x, cos, sin, mask, index), inputs=self.weights.w)
                      for index in range(32)] if not streaming else []

    def _layer(self, x, cos, sin, mask, index):
        w, p = self.weights, f"layers.{index}."
        a = p + "self_attn."
        y = text_norm(x, w.w[p + "input_layernorm.weight"].astype(x.dtype))
        if self.precision == "balanced":
            y = y.astype(mx.bfloat16)
        if a + "qkv_proj.weight" in w.w:
            q, k, v = mx.split(w.linear(a + "qkv_proj", y), [4096, 5120], axis=-1)
        else:
            q, k, v = [w.linear(a + part + "_proj", y) for part in ("q", "k", "v")]
        q = q.reshape(1, -1, 32, 128)
        k = k.reshape(1, -1, 8, 128)
        v = v.reshape(1, -1, 8, 128).transpose(0, 2, 1, 3)
        q = text_norm(q.astype(self.dtype), w.w[a + "q_norm.weight"].astype(self.dtype)).transpose(0, 2, 1, 3)
        k = text_norm(k.astype(self.dtype), w.w[a + "k_norm.weight"].astype(self.dtype)).transpose(0, 2, 1, 3)
        q, k = text_rope(q, cos, sin), text_rope(k, cos, sin)
        if self.precision == "scaled":
            v = v.astype(mx.float16)
        q, k = q.astype(v.dtype), k.astype(v.dtype)
        out = mx.fast.scaled_dot_product_attention(q, k, v, scale=128**-0.5, mask=mask)
        x = x + w.linear(a + "o_proj", out.transpose(0, 2, 1, 3).reshape(1, -1, 4096))
        y = text_norm(x, w.w[p + "post_attention_layernorm.weight"].astype(x.dtype))
        if self.precision == "balanced":
            y = y.astype(mx.bfloat16)
        if p + "mlp.gate_up_proj.weight" in w.w:
            gate, up = mx.split(w.linear(p + "mlp.gate_up_proj", y), 2, axis=-1)
        else:
            gate, up = w.linear(p + "mlp.gate_proj", y), w.linear(p + "mlp.up_proj", y)
        product = (nn.silu(gate.astype(self.dtype)) * up.astype(self.dtype)).astype(gate.dtype)
        return x + w.linear(p + "mlp.down_proj", product)

    def encode(self, input_ids, positions, valid):
        length = len(input_ids)
        if self.streaming:
            w = Weights(load_embedding_rows(self.model_dir / "text_encoder/embedding.safetensors", input_ids), **self.spec)
            x = w.embedding(mx.arange(length))[None].astype(self.dtype)
            mx.eval(x)
            del w
        else:
            x = self.weights.embedding(mx.array(input_ids, dtype=mx.int32))[None].astype(self.dtype)
        # All three MRoPE axes use identical positions for text-only input.
        inv = (1. / (5000000. ** (np.arange(0, 128, 2, dtype=np.float32) / 128))).astype(np.float32)
        angle = np.asarray(positions, dtype=np.float32)[:, None] * inv[None]
        angle = np.concatenate([angle, angle], axis=-1)
        cos, sin = [mx.array(f(angle))[None, None].astype(self.dtype) for f in (np.cos, np.sin)]
        index = mx.arange(length)
        mask = ((index[:, None] >= index[None, :]) & mx.array(valid, dtype=mx.bool_)[None, :])[None, None]
        taps = []
        for i in range(32):
            if self.streaming:
                self.weights = Weights(mx.load(str(self.model_dir / "text_encoder" / f"layer-{i:02d}.safetensors")), **self.spec)
                mx.eval(self.weights.w)
                layer = mx.compile(lambda x, cos, sin, mask: self._layer(x, cos, sin, mask, i), inputs=self.weights.w)
            else:
                layer = self.layer[i]
            x = layer(x, cos, sin, mask)
            if self.streaming:
                mx.eval(x)
                del layer
                self.weights = None
            if (i + 1) % 4 == 0:
                taps.append(x)
        tokens = mx.stack(taps, axis=2).reshape(length, 20480).astype(self.dtype)
        mx.eval(tokens)
        return tokens
