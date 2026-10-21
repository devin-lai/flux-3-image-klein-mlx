# Final preset validation and earlier timing

Archived quality results cover all 12 selection cases and all 10 validation cases against official-code FP32 at 16 steps. The validation set has been inspected repeatedly; it is not untouched holdout evidence. A pass requires mean LPIPS no worse than the official BF16 anchor, mean PSNR and SSIM no lower, and maximum LPIPS no worse than the worst BF16/FP8 anchor for that split. This is an aggregate gate, not pixel equivalence or a promise that every image beats its BF16 counterpart.

The BF16 anchor uses published official images where available and an official-policy BF16 MPS replay for the remaining cases. This differs from the accelerated MLX BF16 configuration in the current 32 GiB report. Numerical anchor values and all per-image scores are included in the result data.

| Preset | Split | Cases | Mean PSNR dB | Mean SSIM | Mean LPIPS | Maximum LPIPS | Gate |
|---|---|---:|---:|---:|---:|---:|---|
| BF16 / 11 steps / fast | selection | 12 | 37.177 | 0.985513 | 0.009738 | 0.022392 | pass |
| BF16 / 11 steps / fast | holdout | 10 | 37.723 | 0.983112 | 0.009792 | 0.022850 | pass |
| BF16 / 11 steps / fused | selection | 12 | 37.187 | 0.985527 | 0.009756 | 0.022397 | pass |
| BF16 / 11 steps / fused | holdout | 10 | 37.863 | 0.983417 | 0.009488 | 0.021913 | pass |
| Q8 + BF16 text / 11 steps | selection | 12 | 36.171 | 0.983293 | 0.010965 | 0.024358 | pass |
| Q8 + BF16 text / 11 steps | holdout | 10 | 36.647 | 0.977749 | 0.013189 | 0.049028 | pass |
| Q8 + BF16 text / 12 steps | selection | 12 | 37.899 | 0.988857 | 0.007038 | 0.013875 | pass |
| Q8 + BF16 text / 12 steps | holdout | 10 | 38.230 | 0.983333 | 0.009926 | 0.046685 | pass |
| Q8 + Q8 text / 13 steps | selection | 12 | 36.492 | 0.985052 | 0.009041 | 0.025194 | pass |
| Q8 + Q8 text / 13 steps | holdout | 10 | 37.028 | 0.976332 | 0.015749 | 0.077112 | pass |
| Hybrid Q8 / 12 steps / archived | selection | 12 | 36.630 | 0.983985 | 0.010388 | 0.032721 | pass |
| Hybrid Q8 / 12 steps / archived | holdout | 10 | 37.976 | 0.984643 | 0.009565 | 0.032509 | pass |

The final 11-step grid is `[0,1,2,3,4,5,6,8,12,13,15,16]`. The 12-step fallback inserts index 10. Q8 with quantized text uses the validated 13-step grid `[0,1,2,3,4,5,6,7,8,10,12,13,15,16]`. These are indices into the official **16-step** time grid, including endpoints. A regular 11-, 12- or 13-step schedule is a different setting. [Presets](../PRESETS.md) record the final choices.

The archived hybrid Q8 12-step alternative passed both splits but did not beat the selected 11-step options on measured latency. Its images and conclusions are retained for completeness; its additional weight export is not in this release. The released Q8 + BF16 text 12-step preset supplies the conservative fallback. BF16 fused/fast and 128/512 MiB cache results are also retained without duplicating weights.

## Earlier Apple M5 Pro, 64 GiB timing

These results are historical and must not be mixed with the current Apple M5, 32 GiB timing. TF32 was enabled in these recorded runs; current local runs disable it. Three fresh-process repeats per case, two timed workloads: 1024 × 1024 photo and 768 × 512 reference edit. No storage-cold or service-throughput claim is made.

### Round optimized-20261020

| Preset | Photo median s | Edit median s | Geomean s | Max physical GiB |
|---|---:|---:|---:|---:|
| bf16-fused-11 | 25.37 | 17.63 | 21.15 | 12.33 |
| bf16-11 | 24.98 | 17.29 | 20.78 | 12.44 |
| bf16-11-cache128 | 25.70 | 17.64 | 21.29 | 12.02 |
| q8-quality-11 | 27.45 | 19.11 | 22.90 | 7.37 |

### Round final-m5pro

| Preset | Photo median s | Edit median s | Geomean s | Max physical GiB |
|---|---:|---:|---:|---:|
| q8-quality-11 | 26.61 | 18.64 | 22.27 | 7.35 |
| q8-quality-11-cache128 | 26.97 | 19.15 | 22.72 | 7.03 |
| q8-quality-12 | 28.80 | 20.28 | 24.17 | 7.36 |
| hybrid-q8-12-archived | 28.45 | 19.94 | 23.82 | 10.60 |
| q8-13 | 31.04 | 21.69 | 25.95 | 7.39 |
| q8 | 37.84 | 26.40 | 31.60 | 7.40 |
| bf16 | 36.12 | 25.78 | 30.52 | 12.37 |

The selected BF16-11 fast/512 MiB configuration measured 20.78 s and 12.44 GiB maximum physical footprint; Q8 + BF16 text at 11 steps measured 22.90 s and 7.37 GiB in the same final round. BF16 fast was 1.72% faster than the fused control. The fast 128 MiB setting reduced the observed memory peak to 12.02 GiB but increased latency to 21.29 s. These small differences are hardware- and round-specific. Denoising dominated that selected configuration: about 90.6% of photo launch time and 88.0% of edit launch time, with median denoising durations 22.66 s and 15.25 s respectively.

The tested 10-step subsets did not satisfy the fixed quality gate. This supports retaining 11 steps for the selected configurations, not a claim that every possible 10-step schedule must fail. Mixed/Q4 and very low-bit candidates did not establish a better validated quality frontier. No conversion method or search history is distributed.

[Complete 22-case image stacks](../gallery/README.md#archived-validation) · [Quality results](../results/historical-validation.json) · [Historical timing data](../results/historical-timing.json).
