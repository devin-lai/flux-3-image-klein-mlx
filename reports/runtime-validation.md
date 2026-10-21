# Standalone inference-loader validation

The released inference-only loader was built as a Python wheel and tested from a separate installation directory with no private package on its Python import path. The wheel contained code and its license, with no model weights.

**All ten checks reproduced the recorded benchmark PNG bytes exactly** on the MacBook Pro M5 / 32 GiB machine:

- All nine finalized presets on the 640 × 640 typography case: BF16/Q8 quality/Q8/mixed/Q4 at 16 steps, BF16 at 11 steps, Q8 quality at 11/12 steps and Q8 at 13 steps.
- Q8 quality at 16 steps on the 768 × 512 reference-image editing case.

Each check used the published prompt, seed, dimensions, model components and timestep grid. The five numerical implementation modules were preserved exactly from the evaluated runtime; the public entry point, paths, cache handling and diagnostic output were adapted for standalone use. Conversion, calibration and search code are absent from the public package.

The [machine-readable checks](../results/runtime-validation.json) identify every expected image and SHA-256 digest. These are packaging parity checks, not new latency measurements or a new subjective-quality study. The original [120-run performance and quality report](macbook-pro-32gb.md) remains the timing evidence. New prompts, seeds and other machines may produce different images and performance.

[Installation and generation](../USAGE.md) · [Model selection](../MODEL_SELECTION.md) · [Image stacks](../gallery/README.md)
