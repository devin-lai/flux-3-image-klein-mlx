# Final inference presets

Weight precision, arithmetic and step count are separate choices. The settings below are declarative; a compatible runtime is required. No inference or conversion implementation is included. The machine-readable counterpart is [presets.json](presets.json).

| Preset | Transformer / text | Steps | Schedule | Purpose and evidence |
|---|---|---:|---|---|
| q8-quality-16 | Q8 / BF16 | 16 | Official | Default fidelity/memory balance; current 32 GiB comparison |
| bf16-16 | BF16 / BF16 | 16 | Official | Closest accelerated control |
| q8-16 | Q8 / Q8 | 16 | Official | Smaller text download; current comparison |
| mixed-16 | Mixed 4/8 / Q8 | 16 | Official | Lower memory, larger fidelity tradeoffs |
| q4-16 | Q4 / Q8 | 16 | Official | Smallest shipped transformer, larger fidelity tradeoffs |
| bf16-11 | BF16 / BF16 | 11 | G11 | Historical fastest validated configuration; local four-case recheck |
| q8-quality-11 | Q8 / BF16 | 11 | G11 | Lower-memory validated 11-step option; local recheck |
| q8-quality-12 | Q8 / BF16 | 12 | G12 | Conservative validated fallback; local recheck |
| q8-13 | Q8 / Q8 | 13 | G13 | Validated reduced-step option with Q8 text; local recheck |
| bf16-fused-11 | BF16 / BF16 | 11 | G11 | Archived kernel alternative; same weights |
| mixed-preview-6 / mixed-preview-8 | Mixed 4/8 / Q8 | 6 / 8 | Official for that step count | Archived speed previews; no FP32-16 equivalence claim |
| q8-preview-8 / q4-preview-8 / bf16-preview-8 | Corresponding weights | 8 | Official for 8 steps | Archived comparison settings |
| fp32-16 | Released BF16 values, upcast | 16 | Official | Strict FP32 arithmetic diagnostic baseline |

- **G11:** `[0,1,2,3,4,5,6,8,12,13,15,16]`.
- **G12:** `[0,1,2,3,4,5,6,8,10,12,13,15,16]`.
- **G13:** `[0,1,2,3,4,5,6,7,8,10,12,13,15,16]`.

These lists select entries of the official 16-step time grid, including start/end. They must not be interpreted as uniform schedules of the same length. The selected final schedules are published usage parameters; the procedure used to discover them is private.

Current local accelerated presets use scaled FP16 matrix arithmetic, FP32 conditioning/residual/integration, FP16 VAE, streamed text layers and a 512 MiB allocation cache. `fast` is used for 16-step runs and BF16-11; `fused` for Q8-11/12/13. Current local measurements disable TF32. Archived 64 GiB timing receipts record TF32 enabled; the full-validation results come from the earlier runtime. Quality transfer across settings is limited to the explicit rechecks in the report.

The 128 MiB cache alternative is recorded in the historical timing report; it is not universally faster. No weights need to be duplicated when changing a step count, schedule, cache limit or kernel mode.

[Final conclusions](RESULTS.md) · [All image stacks](gallery/README.md)
