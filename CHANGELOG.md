# Changelog

## 0.1.0 — 2026-10-21

Initial GitHub source release:

- Native MLX/Metal inference runtime for FLUX.3 Image Klein generation and reference-image editing.
- Five complete pretrained Hugging Face configurations and nine finalized inference presets.
- Custom fused kernels, streamed text layers and sequential model lifetimes.
- Published 120-run M5/32 GiB benchmark, archived 22-case quality validation and original image comparisons.
- Fresh-process community benchmark runner and an audit of the published numerical aggregates.
- Code-only Python packaging, CI checks, issue templates, implementation guide and launch assets.

The measured Q8-quality-16 configuration ran 4.16× faster than the strict MLX FP32 reference and used 7.46 GiB maximum process footprint. The 11-step preset measured 5.43× against that reference in a later round. See the benchmark report for conditions and limits.

Runtime code is Apache-2.0. Separate model-weight license terms apply.
