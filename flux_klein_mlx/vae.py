"""NHWC autoencoder, with global group normalization and query-sliced attention."""
from __future__ import annotations

import mlx.core as mx
import mlx.nn as nn
import numpy as np

from .storage import EXPORT_ROOT
from .fast_kernels import group_norm


class AutoEncoder:
    def __init__(self, encoder=False, dtype=mx.float16, *, fused=False, conv_rows=0, conv_min_pixels=1024**2):
        name = "vae_encoder" if encoder else "vae"
        values = mx.load(str(EXPORT_ROOT / "vae-fp32" / f"{name}.safetensors"))
        self.bn_mean, self.bn_var = values["bn.running_mean"], values["bn.running_var"]
        self.w = {k: v.astype(dtype) for k, v in values.items() if not k.startswith("bn.")}
        self.dtype = dtype
        self.fused = fused
        # conv_rows > 0 evaluates large 3x3 convolutions in row bands with a one-row
        # halo, bounding convolution workspace; normalization and attention stay global.
        self.conv_rows, self.conv_min_pixels = conv_rows, conv_min_pixels
        self.blocks, self.bands = {}, {}
        mx.eval(self.w, self.bn_mean, self.bn_var)

    def sliced(self, x, name, stride=1, padding=1):
        return (self.conv_rows and stride == padding == 1 and x.shape[1] > self.conv_rows
                and x.shape[1] * x.shape[2] >= self.conv_min_pixels and self.w[name + ".weight"].shape[1:3] == (3, 3))

    def conv(self, x, name, stride=1, padding=1):
        if self.sliced(x, name, stride, padding):
            if name not in self.bands:
                self.bands[name] = mx.compile(lambda band: mx.conv2d(band, self.w[name + ".weight"], padding=(0, 1))
                                              + self.w[name + ".bias"])
            parts = []
            for start in range(0, x.shape[1], self.conv_rows):
                end = min(start + self.conv_rows, x.shape[1])
                band = x[:, max(0, start - 1):min(x.shape[1], end + 1)]
                band = mx.pad(band, [(0, 0), (int(start == 0), int(end == x.shape[1])), (0, 0), (0, 0)])
                part = self.bands[name](band)
                mx.eval(part)
                parts.append(part)
            result = mx.concatenate(parts, axis=1)
            mx.eval(result)
            return result
        return mx.conv2d(x, self.w[name + ".weight"], stride=stride, padding=padding) + self.w[name + ".bias"]

    def norm(self, x, name, silu=False):
        if self.fused:
            return group_norm(x, self.w[name + ".weight"], self.w[name + ".bias"], silu=silu)
        b, h, w, c = x.shape
        y = x.astype(mx.float32).reshape(b, h * w, 32, c // 32).transpose(0, 2, 1, 3).reshape(b, 32, -1)
        y = mx.fast.layer_norm(y, None, None, 1e-6)
        y = y.reshape(b, 32, h * w, c // 32).transpose(0, 2, 1, 3).reshape(x.shape)
        y = (y * self.w[name + ".weight"].astype(mx.float32) + self.w[name + ".bias"].astype(mx.float32)).astype(x.dtype)
        return nn.silu(y) if silu else y

    def _block(self, x, name):
        h = self.conv(self.norm(x, name + ".norm1", silu=True), name + ".conv1")
        h = self.conv(self.norm(h, name + ".norm2", silu=True), name + ".conv2")
        if name + ".nin_shortcut.weight" in self.w:
            x = self.conv(x, name + ".nin_shortcut", padding=0)
        return x + h

    def block(self, x, name):
        if self.conv_rows and x.shape[1] * x.shape[2] >= self.conv_min_pixels:
            # Banded convolutions evaluate eagerly, so this block cannot be one compiled graph.
            x = self._block(x, name)
            mx.eval(x)
            return x
        if name not in self.blocks:
            self.blocks[name] = mx.compile(lambda x: self._block(x, name))
        x = self.blocks[name](x)
        mx.eval(x)
        return x

    def attention(self, x, name):
        h = self.norm(x, name + ".norm")
        shape = h.shape
        q, k, v = [self.conv(h, name + "." + key, padding=0).reshape(1, 1, -1, shape[-1])
                   for key in ("q", "k", "v")]
        parts = []
        for start in range(0, q.shape[2], 512):
            out = mx.fast.scaled_dot_product_attention(q[:, :, start:start + 512], k, v, scale=shape[-1]**-0.5)
            mx.eval(out)
            parts.append(out)
        h = mx.concatenate(parts, axis=2).reshape(shape)
        result = x + self.conv(h, name + ".proj_out", padding=0)
        mx.eval(result)
        return result

    def decode(self, tokens, height, width):
        h, w = height // 16, width // 16
        z = tokens.astype(mx.float32).reshape(1, h, w, 128)
        z = z * mx.sqrt(self.bn_var + 1e-4) + self.bn_mean
        z = z.reshape(1, h, w, 32, 2, 2).transpose(0, 1, 4, 2, 5, 3).reshape(1, h * 2, w * 2, 32)
        x = self.conv(self.conv(z.astype(self.dtype), "decoder.post_quant_conv", padding=0), "decoder.conv_in")
        x = self.block(x, "decoder.mid.block_1")
        x = self.attention(x, "decoder.mid.attn_1")
        x = self.block(x, "decoder.mid.block_2")
        for level in reversed(range(4)):
            for block in range(3):
                x = self.block(x, f"decoder.up.{level}.block.{block}")
            if level:
                x = self.conv(mx.repeat(mx.repeat(x, 2, axis=1), 2, axis=2), f"decoder.up.{level}.upsample.conv")
                mx.eval(x)
        image = self.conv(self.norm(x, "decoder.norm_out", silu=True), "decoder.conv_out")[0].astype(mx.float32)
        mx.eval(image)
        return image

    def encode(self, image, *, output_dtype=mx.bfloat16):
        x = self.conv(image[None].astype(self.dtype), "encoder.conv_in")
        for level in range(4):
            for block in range(2):
                x = self.block(x, f"encoder.down.{level}.block.{block}")
            if level < 3:
                x = self.conv(mx.pad(x, [(0, 0), (0, 1), (0, 1), (0, 0)]),
                              f"encoder.down.{level}.downsample.conv", stride=2, padding=0)
                mx.eval(x)
        x = self.block(x, "encoder.mid.block_1")
        x = self.attention(x, "encoder.mid.attn_1")
        x = self.block(x, "encoder.mid.block_2")
        mean = self.conv(self.conv(self.norm(x, "encoder.norm_out", silu=True), "encoder.conv_out"),
                         "encoder.quant_conv", padding=0)[..., :32].astype(mx.float32)
        h, w = mean.shape[1] // 2, mean.shape[2] // 2
        tokens = mean.reshape(1, h, 2, w, 2, 32).transpose(0, 1, 3, 5, 2, 4).reshape(h * w, 128)
        tokens = (tokens - self.bn_mean) * mx.rsqrt(self.bn_var + 1e-4)
        mx.eval(tokens)
        return tokens.astype(output_dtype)
