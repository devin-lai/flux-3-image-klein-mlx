# Archived 6- and 8-step previews

These earlier Apple M5 / 32 GiB results compare with **official-code FP32 at 8 steps**, not the FP32-16 control. They retain the earlier runtime and TF32 setting. They are useful preview tradeoffs and historical comparisons, not current recommendations for FP32-16 fidelity. Three repeats were used for optimized variants; each FP32 baseline had one measured run. Timing included historical integrity-verification and diagnostic-output costs, so do not merge these numbers with the current benchmark.

The images are the archived repeat-mean RGB PNGs used by the archived score report. They are not presented as individual raw generations. Repeat determinism flags, ranges and reference identity are preserved in the data. Smaller step counts can change composition and detail substantially. Earlier mixed-8 and mixed-6 speed choices remain preview options; the full-validation 11/12/13-step presets supersede them for closer FP32-16 reference fidelity.

| Case | Preset | Steps | Median s | Max physical GiB | PSNR vs FP32-8 dB | SSIM vs FP32-8 |
|---|---|---:|---:|---:|---:|---:|
| man_dog | official-fp32-8 | 8 | 376.92 | 9.69 | ∞ | 1.000000 |
| man_dog | previous-q8-8 | 8 | 44.34 | 6.82 | 31.03 | 0.960284 |
| man_dog | previous-q4-8 | 8 | 36.65 | 6.19 | 19.14 | 0.669131 |
| man_dog | q8-8 | 8 | 44.00 | 6.74 | 37.00 | 0.988010 |
| man_dog | q4-8 | 8 | 36.63 | 5.36 | 25.59 | 0.860017 |
| man_dog | mixed-8 | 8 | 42.19 | 5.53 | 25.26 | 0.871322 |
| man_dog | bf16-8 | 8 | 55.38 | 10.95 | 42.77 | 0.996176 |
| man_dog | mixed-6 | 6 | 25.99 | 5.56 | 22.48 | 0.769897 |
| teapot_small | official-fp32-8 | 8 | 160.37 | 4.62 | ∞ | 1.000000 |
| teapot_small | previous-q8-8 | 8 | 15.53 | 6.15 | 36.27 | 0.988893 |
| teapot_small | previous-q4-8 | 8 | 14.13 | 3.93 | 22.61 | 0.836463 |
| teapot_small | q8-8 | 8 | 16.32 | 6.21 | 37.75 | 0.989775 |
| teapot_small | q4-8 | 8 | 15.12 | 4.28 | 29.24 | 0.946049 |
| teapot_small | mixed-8 | 8 | 14.33 | 5.01 | 30.83 | 0.962304 |
| teapot_small | bf16-8 | 8 | 16.94 | 10.49 | 55.84 | 0.999334 |
| teapot_small | mixed-6 | 6 | 9.72 | 5.00 | 26.66 | 0.910191 |
| poster_small | official-fp32-8 | 8 | 187.20 | 4.64 | ∞ | 1.000000 |
| poster_small | previous-q8-8 | 8 | 17.16 | 6.30 | 26.62 | 0.940932 |
| poster_small | previous-q4-8 | 8 | 15.62 | 4.13 | 20.42 | 0.789526 |
| poster_small | q8-8 | 8 | 17.32 | 6.23 | 29.21 | 0.968953 |
| poster_small | q4-8 | 8 | 17.48 | 4.41 | 23.02 | 0.881681 |
| poster_small | mixed-8 | 8 | 16.12 | 5.13 | 23.29 | 0.882768 |
| poster_small | bf16-8 | 8 | 18.17 | 10.51 | 27.53 | 0.952900 |
| poster_small | mixed-6 | 6 | 10.79 | 5.14 | 23.08 | 0.877338 |
| teapot_edit_small | official-fp32-8 | 8 | 277.44 | 4.62 | ∞ | 1.000000 |
| teapot_edit_small | previous-q8-8 | 8 | 28.69 | 7.05 | 51.02 | 0.997847 |
| teapot_edit_small | previous-q4-8 | 8 | 25.82 | 4.54 | 35.80 | 0.983376 |
| teapot_edit_small | q8-8 | 8 | 27.97 | 7.32 | 56.46 | 0.999030 |
| teapot_edit_small | q4-8 | 8 | 25.13 | 5.15 | 38.61 | 0.990404 |
| teapot_edit_small | mixed-8 | 8 | 26.82 | 5.96 | 42.74 | 0.996017 |
| teapot_edit_small | bf16-8 | 8 | 31.57 | 12.25 | 60.41 | 0.999576 |
| teapot_edit_small | mixed-6 | 6 | 18.19 | 5.95 | 42.82 | 0.994695 |

Previous Q8/Q4 images document the earlier precision path; those older weights are not shipped. [Preview stacks](../gallery/README.md#archived-previews) and [result data](../results/preview-history.json) preserve the final observations.
