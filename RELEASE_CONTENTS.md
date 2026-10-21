---
license: other
license_name: flux-kommunity
license_link: LICENSE.md
base_model: black-forest-labs/flux-3-image-klein
tags:
  - mlx
  - safetensors
  - text-to-image
  - image-to-image
  - apple-silicon
---

# flux-3-image-klein-mlx

This document describes the original combined local package and its component layout. On Hugging Face, the main repository contains the runtime, documentation and gallery; each standalone variant repository contains only its selected model components. See the [Hugging Face model card](https://huggingface.co/devin-lai/flux-3-image-klein-mlx) for the download links. This is an independent repacked and quantized derivative. Original attribution and license files accompany the weights.

This package contains safetensors weights, loading metadata, tokenizer assets, final inference presets, benchmark reports, experimental conclusions and image stacks. An inference-only MLX loader is included. Conversion and calibration code and experimental workflows remain undisclosed.

## Run a model

Follow the [installation and generation guide](USAGE.md), then select a preset using the [model guide](MODEL_SELECTION.md) and [image stacks](gallery/README.md). The included loader supports all five released weight configurations and the finalized 11/12/13-step presets.

## Results and image comparisons

- [Final conclusions](RESULTS.md): recommendations, tradeoffs and tested limits.
- [MacBook Pro M5 / 32 GiB test report](reports/macbook-pro-32gb.md): MLX FP32 baseline and five optimized configurations at 16 steps, plus the finalized 11/12/13-step presets.
- [Final presets](PRESETS.md) and [machine-readable settings](presets.json): exact retained step grids, weight/text combinations and measured runtime settings.
- [22-case validation and earlier M5 Pro / 64 GiB timing](reports/validated-presets.md): kept separate from current local measurements.
- [Archived 6/8-step conclusions](reports/preview-history.md): preview tradeoffs against the earlier FP32-8 reference.
- [Image stacks](gallery/README.md): complete prompts, seeds, reference inputs, labeled contact sheets and original PNGs across parameter settings.

The local tests include 120 fresh-process measurements: 72 at 16 steps and 48 for four reduced-step presets. Results include latency ranges, physical memory, MLX allocation, PSNR, SSIM, LPIPS and repeat determinism. The [result data](results/m5-32gb-16step.json) and [preset data](results/m5-32gb-presets.json) are portable and omit private paths and implementation receipts.

## Variants

| Variant | Transformer directory | Text directory | Complete download | Intended use |
|---|---|---|---:|---|
| bf16 | bf16 | bf16 | 17.40 GiB | Unquantized weight control; accelerated inference. |
| q8-quality | q8 | bf16 | 12.73 GiB | 8-bit transformer with unquantized text features. |
| q8 | q8 | q8 | 9.58 GiB | 8-bit transformer and text features; smaller download. |
| mixed | mixed | q8 | 8.23 GiB | Mixed 4/8-bit transformer; reduced memory with fidelity tradeoffs. |
| q4 | q4 | q8 | 7.40 GiB | Smallest transformer; larger fidelity tradeoffs. |

The download figures include the image-conditioning weights, text encoder, shared tokenizer and FP32 autoencoder. Text-only generation can omit the image-conditioning component. `q8-quality` shares its transformer with `q8` and its text encoder with `bf16`; it is a component selection, not another weight copy. The mixed and Q4 variants share the Q8 text encoder. Stored precision is separate from inference arithmetic and step count.

Start with `q8-quality` when fidelity to the unquantized model matters. `q8` reduces the text-encoder download, while mixed and Q4 prioritize smaller transformer storage and lower memory. Those compact variants can change composition and object counts; for example, Q4 added a second pencil in the local typography test. They are not represented as FP32-equivalent. `bf16` preserves unquantized weight values for the highest-fidelity comparison.

## Loading contract

`model_index.json` lists each variant's component paths. Each component manifest lists safetensors paths, sizes and SHA-256 checksums. Quantized tensor entries give the bit width and group size required by MLX affine quantized matrix multiplication. Dense conditioning and normalization tensors retain their stored types. The autoencoder is stored in FP32.

The `fluxmac-packed-v1` layout groups transformer tensors by block and includes packed projections. The included `flux_klein_mlx` loader reads this layout directly. This is not a drop-in Diffusers pipeline or a complete Qwen3-VL checkpoint. The text encoder contains the first 32 layers used for image conditioning; `assets/config.json` is the original upstream configuration and describes the larger source architecture. The loader runs locally and does not import conversion code or download executable remote code.

The official 16-step schedule is the default reference comparison. The finalized reduced-step presets retain selected entries of that same grid; use their explicit settings in `presets.json`. The local benchmark distinguishes unquantized BF16 storage with accelerated arithmetic from the strict FP32 arithmetic baseline; no duplicate FP32 checkpoint is distributed. The original released BF16 checkpoint values are upcast for that baseline.

## Integrity and provenance

Upstream checkpoint revision: `1755314e2216b2a2c5cc0dd899d4e49ee3404d2c`. `assets/source-manifest.json` records the source transformer checksum. Each repository's `SHA256SUMS` covers its payload, including reports and images when present; it excludes itself and the outer `release-manifest.json`. The outer manifest also hashes `SHA256SUMS`. `publication.json` inventories the public source package material; some entries describe files in the original combined local package. `runtime.json` inventories the inference code. Safetensors are configured for Git LFS/Xet. Standalone variant repositories each include their needed components, even when other variants use the same components.

The finalized release is independent of private development files. Identical tensor files within this local release share regular-file hard links. Treat these tensors as immutable: replace files when making a new export; do not overwrite linked tensors in place. Uploaded/downloaded files do not depend on any private local path.

## License and attribution

FLUX weights retain the [FLUX Kommunity License](licenses/FLUX-KOMMUNITY.md) and [attribution notice](NOTICE.md). The text encoder assets retain their [Apache-2.0 license](LICENSE-text-encoder.txt). The inference runtime is distributed under [Apache-2.0](LICENSE-runtime.txt); upstream runtime attribution is retained in the notice. Public availability does not replace these upstream terms with an unrestricted software license. This package is not an official Black Forest Labs release.
