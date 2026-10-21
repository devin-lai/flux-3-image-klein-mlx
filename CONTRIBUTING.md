# Contributing

Help make local image generation easier to reproduce across Apple Silicon Macs. Useful contributions include installation fixes, new Mac benchmark reports, tests for real failures, kernel improvements with numerical evidence, and clearer examples.

## Report a problem

Use [GitHub issues](https://github.com/devin-lai/flux-3-image-klein-mlx/issues/new/choose). Include your chip, unified memory, macOS, Python/package versions, variant, preset, command and complete error. Remove tokens, private prompts and personal paths. For output problems, include prompt, seed, dimensions and reference input when shareable.

## Submit a change

1. Fork the repository and create a branch.
2. Keep the change focused and explain the user-visible result.
3. Run `python -m unittest discover -s tests` and `python scripts/audit_benchmarks.py`.
4. For numerical changes, compare outputs against the published prompts/seeds and document the changed arithmetic and quality metrics. For performance changes, record hardware, process/cache conditions and repeated measurements.
5. Open a pull request with validation and any limitations.

Software tests do not replace Metal inference validation. Do not edit archived benchmark records to improve a headline. New measurements belong in a separate report with provenance.

## Share your Mac benchmark

Run the [benchmark guide](benchmarks/README.md), then use the benchmark issue template. Reports from additional chips and memory capacities are especially valuable. Negative results and installation failures help establish supported configurations.

Code contributions are under Apache-2.0. Preserve upstream attribution and keep model weights out of Git. Follow the separate model license when using or sharing generated outputs.
