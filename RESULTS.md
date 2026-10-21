# Final conclusions

The release includes four transformer exports and five component combinations, final inference presets, measured test results, and parameter-labeled image stacks. Conversion/calibration code, private runtime source and experimental workflows remain undisclosed.

- **Start with Q8 + BF16 text at 16 steps for strong reference fidelity.** On Apple M5 / 32 GiB it measured 38.75 s across the four workloads, 4.16× the FP32 baseline speed, 7.46 GiB maximum physical footprint and mean LPIPS 0.003246. This is a measured configuration comparison, not a claim of pixel equivalence.
- **BF16 at 16 steps is the closest accelerated control:** mean PSNR 54.12 dB and LPIPS 0.000174 versus MLX FP32. The strict MLX FP32-16 baseline itself measured 161.16 s and 12.98 GiB. The independent official-code FP32 comparison differs by no more than one 8-bit channel code.
- **Keep the validated reduced-step choices.** BF16 at 11 steps and Q8 + BF16 text at 11 steps passed both archived full splits (22 images). Q8 + BF16 text at 12 steps is the conservative fallback. Q8 + Q8 text at 13 steps also passed both splits and uses the smaller text-encoder download. The current Mac recheck covers four cases for each; it does not replace the full archived validation.
- **Q8 with quantized text reduces download size; mixed and Q4 reduce memory further.** They are useful capacity tradeoffs. Mixed/Q4 can change layout, contours and object counts. At 16 steps, Q4 added a second red pencil to a prompt requesting one. These compact alternatives are not certified as FP32-16 equivalent.
- **Retain 6/8-step settings as previews.** Earlier mixed-8 and mixed-6 results are included, with their FP32-8 reference and previous-runtime conditions. They do not establish FP32-16 fidelity. Tested 10-step subsets failed the fixed full-quality requirement; no universal step-count floor is inferred.
- **The historical fastest validated point was BF16-11 on M5 Pro / 64 GiB**, 20.78 s across two workloads, versus 22.90 s and lower memory for Q8 + BF16 text at 11 steps. Those measurements are kept separate from the new M5 / 32 GiB data.

## Current reduced-step observations

| Preset | Launch geomean s | Max physical GiB | PSNR vs MLX FP32-16 dB | SSIM | LPIPS |
|---|---:|---:|---:|---:|---:|
| BF16 / 11 steps / fast | 30.99 | 12.43 | 38.00 | 0.988979 | 0.007941 |
| Q8 + BF16 text / 11 steps | 29.69 | 7.33 | 37.30 | 0.986374 | 0.008134 |
| Q8 + BF16 text / 12 steps | 31.70 | 7.38 | 38.58 | 0.989449 | 0.005936 |
| Q8 + Q8 text / 13 steps | 33.34 | 7.32 | 38.60 | 0.989172 | 0.005671 |

On this M5 / 32 GiB sample, **Q8 + BF16 text / 11 steps** was the fastest of the four finalized reduced-step configurations. Q8 + BF16 text at 12 steps improved the measured reference fidelity over its 11-step setting, with additional latency. Q8 with Q8 text at 13 steps offers a smaller download and another validated quality/speed choice. The hardware-specific ranking differs from the earlier M5 Pro result.

The previous hybrid Q8 12-step export also passed quality validation, but adds another large weight set and did not improve the selected 11-step latency tradeoff. Its final scores and images are preserved as an archived alternative; the release uses shared BF16/Q8 components instead. Cache and kernel alternatives are recorded without additional weight copies.

## Visual observations and scope

The 16-step review found BF16 and Q8 + BF16 text close to the FP32 scene layout. All variants produced coherent images on the four local cases. Printed `EARL GREY`, `MORNING LIGHT` and `STUDIO 27` remained legible in that sample. All variants performed the blue-to-red teapot edit while retaining the surrounding objects. Mixed/Q4 showed larger contour, texture and composition changes; Q4's additional pencil is a concrete prompt-adherence failure.

Visual review of the four new reduced-step stacks found the main photo composition, legible poster lettering, single-pencil layout and intended red-teapot edit retained in these samples. Differences remain in subject contours, object placement, highlights and fine texture. The original PNGs are included so these observations can be checked at full resolution; contact-sheet thumbnails alone do not establish pixel fidelity.

These are qualitative visual observations, not a blinded preference study. Perceptual metrics measure agreement with a fixed reference. They do not prove aesthetic superiority, broad prompt adherence or generalization. Complete per-image results include harder archived cases, so the presentation is not limited to favorable examples.

[32 GiB test report](reports/macbook-pro-32gb.md) · [Archived full validation and 64 GiB timing](reports/validated-presets.md) · [6/8-step history](reports/preview-history.md) · [Presets](PRESETS.md) · [Image stacks](gallery/README.md)
