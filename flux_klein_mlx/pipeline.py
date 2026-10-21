"""Sequential model lifetimes in one native MLX process; no GPU Torch allocator."""
from __future__ import annotations


import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import mlx.core as mx
import numpy as np
from PIL import Image, ImageOps
from tokenizers import Tokenizer

from .common import physical_footprint, write_json
from .storage import EXPORT_ROOT, sha256, verification_cache
from .engine import DiT, TextEncoder, release
from .vae import AutoEncoder


def tokenize(prompt):
    tokenizer = Tokenizer.from_file(str(EXPORT_ROOT / "assets/tokenizer.json"))
    tokenizer.enable_truncation(max_length=4096)
    text = "<|im_start|>user\n" + prompt + "<|im_end|>\n<|im_start|>assistant\n"
    ids = tokenizer.encode(text).ids
    length = min(4096, -(-len(ids) // 80) * 80)
    valid = np.arange(length) < len(ids)
    positions = np.where(valid, np.arange(length), 1)
    ids += [151643] * (length - len(ids))
    return ids, positions, valid


def latent_ids(height, width):
    rows, cols = np.meshgrid(np.arange(height // 16), np.arange(width // 16), indexing="ij")
    return np.stack([np.zeros_like(rows), rows, cols, np.zeros_like(rows)], axis=-1).reshape(-1, 4).astype(np.float32)


def prepare_reference(path, multi):
    with Image.open(path) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
    if multi:
        width, height = image.size
        if width * height > 1024**2:
            scale = (1024**2 / (width * height)) ** 0.5
            width, height = int(width * scale), int(height * scale)
            image = image.resize((width, height), Image.Resampling.LANCZOS)
        w, h = width // 16 * 16, height // 16 * 16
        left, top = (width - w) // 2, (height - h) // 2
        image = image.crop((left, top, left + w, top + h))
    else:
        width, height = image.size
        scale = min(1., (4 * 1024**2 / (width * height)) ** 0.5, 4096 / max(width, height))
        while True:
            fit = max(1, round(width * scale)), max(1, round(height * scale))
            w, h = tuple(min(4096, max(64, -(-v // 16) * 16)) for v in fit)
            if w * h <= 4 * 1024**2:
                break
            scale *= .995
        if fit != image.size:
            image = image.resize(fit, Image.Resampling.LANCZOS)
        if (w, h) != image.size:
            left, top = (w - image.width) // 2, (h - image.height) // 2
            padding = ((top, h - image.height - top), (left, w - image.width - left), (0, 0))
            mode = "reflect" if min(image.size) > 16 else "symmetric"
            image = Image.fromarray(np.pad(np.asarray(image), padding, mode=mode))
    return np.asarray(image, dtype=np.float32) / 127.5 - 1.


def verify_export(model_dir, components=None):
    """Cache file identities; stream hashes after any size/mtime/ctime change."""
    manifests = [Path(model_dir) / "manifest.json", EXPORT_ROOT / "vae-fp32/manifest.json", EXPORT_ROOT / "assets/manifest.json"]
    source_hash = sha256(EXPORT_ROOT / "assets/source-manifest.json")
    cache_path = verification_cache(model_dir)
    previous = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    current = {}
    for manifest_path in manifests:
        manifest = json.loads(manifest_path.read_text())
        if manifest["source_manifest_sha256"] != source_hash:
            raise ValueError(f"Source export changed: {manifest_path}")
        for artifact in manifest["artifacts"]:
            if (components is not None and manifest_path.parent == Path(model_dir)
                    and Path(artifact["path"]).parts[0] not in components):
                continue
            path = manifest_path.parent / artifact["path"]
            stat = path.stat()
            identity = [stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns, artifact["sha256"]]
            if stat.st_size != artifact["bytes"]:
                raise ValueError(f"Truncated model file: {path}")
            if previous.get(str(path)) != identity and sha256(path) != artifact["sha256"]:
                raise ValueError(f"Model checksum mismatch: {path}")
            current[str(path)] = identity
    # Component verification must not evict identities for other valid parts.
    # Atomic replace also prevents concurrent readers seeing truncated JSON.
    partial = cache_path.with_name(f".{cache_path.name}.{os.getpid()}.partial")
    write_json(partial, previous | current)
    partial.replace(cache_path)


def generate(request, output, *, text_bits=None, vae_dtype="float16", vae_rows=0, cache_mb=512,
             dit_dtype="float32", matmul="quantized", kernel_mode="fused", stream_text=True, precision="scaled"):
    model_dir = EXPORT_ROOT / request["transformer"]
    text_dir = EXPORT_ROOT / request["text_encoder"]
    bits = json.loads((model_dir / "manifest.json").read_text())["bits"]
    text_bits = json.loads((text_dir / "manifest.json").read_text())["bits"]
    verification_start = time.perf_counter()
    used = {model_dir: {"transformer"}}
    if request.get("references"):
        used[model_dir].add("image_conditioning")
    used.setdefault(text_dir, set()).add("text_encoder")
    for path, components in used.items():
        verify_export(path, components=components)
    verification_seconds = time.perf_counter() - verification_start
    start = time.perf_counter()
    mx.set_cache_limit(cache_mb * 1024**2)
    mx.reset_peak_memory()
    output = Path(output)
    metrics = {"backend": "mlx", "mlx_version": mx.__version__, "bits": bits, "text_bits": text_bits,
               "quantization_profile": model_dir.name,
               "vae_dtype": vae_dtype, "vae_rows": vae_rows, "cache_limit_bytes": cache_mb * 1024**2,
               "dit_dtype": dit_dtype, "precision": precision, "matmul": matmul, "kernel_mode": kernel_mode, "stream_text": stream_text,
               "mlx_enable_tf32": os.environ.get("MLX_ENABLE_TF32", "1"),
               "arithmetic": dict(matrix="scaled float16" if precision == "scaled" else "float32" if precision == "fp32" else "bfloat16",
                                  conditioning="bfloat16" if precision == "legacy" else "float32",
                                  residuals="bfloat16" if precision == "legacy" else "float32", euler="float32"),
               "device": mx.device_info(),
               "verification_seconds": verification_seconds,
               "model_manifests_sha256": {str(p.relative_to(EXPORT_ROOT)): sha256(p / "manifest.json")
                                            for p in dict.fromkeys((model_dir, text_dir, EXPORT_ROOT / "vae-fp32", EXPORT_ROOT / "assets"))}}
    dtype = {"float16": mx.float16, "float32": mx.float32}[vae_dtype]
    schedule_label = f"official 16-step timesteps {request['grid']}" if request.get("grid") else "official schedule"
    print(f"MLX weights {model_dir.name} ({bits}-bit base); text {text_bits}-bit; arithmetic {precision}; VAE {vae_dtype}; "
          f"{request['steps']} flow-map steps ({schedule_label})", flush=True)
    stages = {}
    memory_stages = {}
    def memory_sample(name):
        memory_stages[name] = dict(active_bytes=mx.get_active_memory(), peak_bytes=mx.get_peak_memory())
    with tempfile.TemporaryDirectory(prefix="flux-klein-") as scratch:
        noise_path = Path(scratch) / "noise.npz"
        # The CPU-only Torch RNG worker runs while text and references are encoded on the GPU.
        noise_worker = subprocess.Popen([sys.executable, "-m", "flux_klein_mlx.noise", "--seed", str(request["seed"]),
                                         "--tokens", str(request["height"] // 16 * (request["width"] // 16)),
                                         "--steps", str(request["steps"]), "--output", str(noise_path)]
                                        + (["--grid", ",".join(map(str, request["grid"]))] if request.get("grid") else []))
        ids, positions, valid = tokenize(request["prompt"])
        metrics["token_ids_sha256"] = hashlib.sha256(np.asarray(ids, dtype=np.int64).tobytes()).hexdigest()
        stage_start = time.perf_counter()
        text_encoder = TextEncoder(text_dir, streaming=stream_text, precision=precision)
        loaded = time.perf_counter()
        text = text_encoder.encode(ids, positions, valid)
        stages["encode"] = dict(load_seconds=loaded - stage_start, compute_seconds=time.perf_counter() - loaded)
        del text_encoder
        release()
        memory_sample("after_text")

        references = request.get("references", [])
        reference, reference_ids = None, None
        if references:
            stage_start = time.perf_counter()
            ae = AutoEncoder(encoder=True, dtype=dtype, fused=kernel_mode != "portable")
            loaded = time.perf_counter()
            tokens, id_parts = [], []
            for index, path in enumerate(references):
                image = prepare_reference(path, len(references) > 1)
                tokens.append(ae.encode(mx.array(image), output_dtype=mx.bfloat16 if precision == "legacy" else mx.float32))
                ri = latent_ids(*image.shape[:2])
                ri[:, 1:3] *= .5
                ri[:, 3] = -(index + 1)
                id_parts.append(ri)
            reference, reference_ids = mx.concatenate(tokens), np.concatenate(id_parts)
            mx.eval(reference)
            stages["references"] = dict(load_seconds=loaded-stage_start, compute_seconds=time.perf_counter()-loaded)
            del ae, tokens
            release()

        if noise_worker.wait():
            raise RuntimeError("Initial-noise worker failed")
        with np.load(noise_path) as data:
            noise, schedule = data["noise"].copy(), data["schedule"].copy()
        stage_start = time.perf_counter()
        transformer = DiT(model_dir, references=bool(references),
                          dtype={"float16": mx.float16, "bfloat16": mx.bfloat16, "float32": mx.float32}[dit_dtype],
                          matmul=matmul, fused="fast" if kernel_mode == "fast" else kernel_mode == "fused", precision=precision)
        loaded = time.perf_counter()
        memory_sample("transformer_loaded")
        image_ids = latent_ids(request["height"], request["width"])
        scaled = image_ids.copy()
        scaled[:, 1:3] *= .5
        mode_ids = {"image": scaled}
        if references:
            mode_ids["image_cond"] = reference_ids
        mode_ids["text"] = np.stack([np.zeros(len(ids))] * 3 + [np.arange(len(ids))], axis=-1)
        transformer.prepare(schedule, mode_ids)
        memory_sample("conditioning_prepared")
        conditioning_seconds = time.perf_counter() - loaded
        image = mx.array(noise)
        step_seconds, first = [], None
        for step in range(request["steps"]):
            step_start = time.perf_counter()
            velocity = transformer(image, text, reference, step)
            image = image + float(schedule[step + 1] - schedule[step]) * velocity.astype(mx.float32)
            mx.eval(image)
            if step == 0:
                memory_sample("first_step")
            step_seconds.append(time.perf_counter() - step_start)
            if not bool(mx.all(mx.isfinite(image)).item()):
                raise ValueError(f"Non-finite latent at step {step + 1}")
            print(f"{request['profile']} step {step + 1}/{request['steps']}: {step_seconds[-1]:.3f}s", flush=True)
        stages["denoise"] = dict(load_seconds=loaded - stage_start, conditioning_seconds=conditioning_seconds,
                                  compute_seconds=conditioning_seconds + sum(step_seconds), step_seconds=step_seconds)
        del transformer, text, reference, first, velocity
        release()
        memory_sample("after_denoise")

        stage_start = time.perf_counter()
        ae = AutoEncoder(dtype=dtype, fused=kernel_mode != "portable", conv_rows=vae_rows)
        loaded = time.perf_counter()
        decoded = ae.decode(image, request["height"], request["width"])
        if not bool(mx.all(mx.isfinite(decoded)).item()):
            raise ValueError("Non-finite decoded image")
        stages["decode"] = dict(load_seconds=loaded - stage_start, compute_seconds=time.perf_counter() - loaded)
        rgb = np.asarray(((mx.clip(decoded, -1, 1) + 1) * 127.5).astype(mx.uint8))
        Image.fromarray(rgb).save(output)
        del ae, decoded, image
        release()
        memory_sample("after_decode")
    metrics.update(stages)
    metrics["wall_seconds"] = time.perf_counter() - start
    metrics["compute_seconds"] = sum(v["compute_seconds"] for v in stages.values())
    metrics["peak_mlx_active_bytes"] = mx.get_peak_memory()
    metrics["memory_stages"] = memory_stages
    metrics.update(physical_footprint())
    return metrics
