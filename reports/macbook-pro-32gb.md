# Benchmark report: MacBook Pro, Apple M5, 32 GiB

The 16-step comparison contains 72 fresh-process measurements (six configurations × four workloads × three repeats). A later confirmation adds 48 measurements for four finalized reduced-step presets. The weights and runtime implementation are identical across these local rounds. The reduced-step timings were measured later, so their speed ratios to FP32 are cross-round observations.

Latency below is the geometric mean of four workload medians. Memory is the maximum process lifetime physical footprint across all twelve runs of a configuration, including Metal allocations. MLX active allocation is reported separately and must not be added to physical memory. Fidelity is the equal-workload mean against MLX FP32 at 16 steps. Smaller LPIPS and larger PSNR/SSIM indicate closer reference agreement, not aesthetic superiority.

## Local results

| Configuration | Launch geomean s | Speedup vs FP32 | Max physical GiB | Max MLX GiB | PSNR dB ↑ | SSIM ↑ | LPIPS ↓ |
|---|---:|---:|---:|---:|---:|---:|---:|
| MLX FP32 / 16 steps | 161.16 | 1.00× | 12.98 | 12.28 | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | 40.34 | 4.00× | 12.47 | 11.74 | 54.12 | 0.999328 | 0.000174 |
| Q8 + BF16 text / 16 steps | 38.75 | 4.16× | 7.46 | 6.75 | 41.80 | 0.993571 | 0.003246 |
| Q8 + Q8 text / 16 steps | 36.65 | 4.40× | 7.43 | 6.75 | 41.02 | 0.991263 | 0.004196 |
| Mixed 4/8 + Q8 text / 16 steps | 34.91 | 4.62× | 6.07 | 5.40 | 29.74 | 0.941386 | 0.046897 |
| Q4 + Q8 text / 16 steps | 33.75 | 4.77× | 5.53 | 5.09 | 28.97 | 0.932710 | 0.054543 |
| BF16 / 11 steps / fast | 30.99 | 5.20×* | 12.43 | 11.74 | 38.00 | 0.988979 | 0.007941 |
| Q8 + BF16 text / 11 steps | 29.69 | 5.43×* | 7.33 | 6.69 | 37.30 | 0.986374 | 0.008134 |
| Q8 + BF16 text / 12 steps | 31.70 | 5.08×* | 7.38 | 6.69 | 38.58 | 0.989449 | 0.005936 |
| Q8 + Q8 text / 13 steps | 33.34 | 4.83×* | 7.32 | 6.69 | 38.60 | 0.989172 | 0.005671 |

*Later round on the same machine; not interleaved with the FP32 control. All 40 configuration/workload groups produced identical PNGs across their three local repeats. These four cases have been used before and do not constitute a new full-suite quality certification.

## Arithmetic and measurement conditions

The FP32 control uses released BF16 checkpoint values upcast to FP32 on demand, FP32 arithmetic, portable kernels, FP32 VAE execution and disabled TF32. Checkpoint storage remains BF16 between operations. On-demand casting is included in timing; a fully FP32-resident checkpoint was not benchmarked. No unpublished FP32 master weights are claimed.

Accelerated configurations use scaled FP16 matrix multiplication, FP32 conditioning/residual/integration calculations and FP16 VAE execution. Stored weight precision and arithmetic precision are distinct. The 16-step runs and BF16-11 use `fast` kernels; Q8-11, Q8-12 and Q8-13 use `fused` kernels. These are configured-pipeline comparisons, not isolated quantization-only experiments. All current local runs disable TF32.

Every request uses a new process, identical prompt/seed/canvas/reference inputs, streamed text layers, a 512 MiB MLX cache, and sequential GPU execution. Filesystem and driver caches are ordinary; integrity caches were populated before timing. There is no retained model or text-conditioning cache across requests. Launch timing includes startup, integrity verification, weight loading, text encoding, denoising, image decoding and PNG output. Process polling has approximately 0.2 s granularity. Three repeats and a five-second gap were used. The 16-step and three-preset rounds rotate order; Q8-13 is its own round. All runs were on AC power; other desktop applications were left running.

Physical memory uses the macOS kernel lifetime process footprint. A sampled process-tree measure also includes the noise worker; sampling at 0.2 s can miss short peaks. Results cover the listed canvases and one-reference edits, not all resolutions or batch sizes. PSNR/SSIM use complete 8-bit RGB images. LPIPS uses AlexNet v0.1 on CPU after GPU timing. No FID, broad prompt-adherence score, energy measurement or blinded human preference score is claimed.

Hardware: Apple M5, 32 GiB, Mac17,2; macOS-27.0.1-arm64-arm-64bit. Python 3.12.10. Runtime versions: mlx 0.32.4; mlx-metal 0.32.4; torch 2.14.1; numpy 2.5.4; safetensors 0.8.0; tokenizers 0.22.2; lpips 0.1.4.

16 steps measurement window: 2026-10-20T23:48:06-04:00 to 2026-10-21T01:09:32-04:00.

Final presets measurement window: 2026-10-21T01:59:25-04:00 to 2026-10-21T02:22:41-04:00.

Final presets measurement window: 2026-10-21T02:23:04-04:00 to 2026-10-21T02:31:15-04:00.

## Workload details

### man_dog: 1024 × 1024, seed 7

[Image stack and complete prompt](../gallery/local/man_dog.md).

| Configuration | Median [min, max] s | Max physical GiB | Sampled tree GiB | PSNR dB | SSIM | LPIPS |
|---|---:|---:|---:|---:|---:|---:|
| MLX FP32 / 16 steps | 277.55 [277.40, 278.82] | 12.31 | 11.99 | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | 70.69 [70.61, 71.93] | 11.06 | 10.95 | 53.39 | 0.999549 | 0.000143 |
| Q8 + BF16 text / 16 steps | 66.61 [66.18, 67.96] | 6.85 | 6.77 | 40.68 | 0.995973 | 0.002346 |
| Q8 + Q8 text / 16 steps | 65.18 [64.36, 65.89] | 6.82 | 6.77 | 39.55 | 0.994783 | 0.003346 |
| Mixed 4/8 + Q8 text / 16 steps | 62.69 [62.37, 63.68] | 5.67 | 5.57 | 26.41 | 0.935084 | 0.050433 |
| Q4 + Q8 text / 16 steps | 60.71 [59.76, 61.34] | 5.53 | 4.84 | 27.48 | 0.936144 | 0.046756 |
| BF16 / 11 steps / fast | 52.93 [52.04, 53.44] | 11.05 | 10.95 | 34.78 | 0.983806 | 0.012697 |
| Q8 + BF16 text / 11 steps | 50.99 [49.08, 51.07] | 6.84 | 6.73 | 34.02 | 0.981402 | 0.014055 |
| Q8 + BF16 text / 12 steps | 54.62 [52.56, 55.05] | 6.73 | 6.66 | 36.06 | 0.987531 | 0.008994 |
| Q8 + Q8 text / 13 steps | 58.18 [55.03, 59.20] | 6.74 | 6.66 | 37.33 | 0.990936 | 0.006361 |

### teapot_small: 768 × 512, seed 1937

[Image stack and complete prompt](../gallery/local/teapot_small.md).

| Configuration | Median [min, max] s | Max physical GiB | Sampled tree GiB | PSNR dB | SSIM | LPIPS |
|---|---:|---:|---:|---:|---:|---:|
| MLX FP32 / 16 steps | 104.66 [104.58, 104.89] | 11.27 | 11.23 | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | 26.68 [26.65, 26.92] | 10.43 | 10.30 | 56.57 | 0.999428 | 0.000115 |
| Q8 + BF16 text / 16 steps | 25.47 [25.33, 25.49] | 6.13 | 6.09 | 37.25 | 0.994718 | 0.003419 |
| Q8 + Q8 text / 16 steps | 23.29 [23.27, 23.36] | 6.13 | 6.05 | 36.24 | 0.990315 | 0.004314 |
| Mixed 4/8 + Q8 text / 16 steps | 22.21 [22.04, 22.39] | 4.91 | 4.83 | 29.65 | 0.969659 | 0.017307 |
| Q4 + Q8 text / 16 steps | 21.35 [21.30, 21.59] | 4.18 | 4.09 | 29.02 | 0.952869 | 0.027506 |
| BF16 / 11 steps / fast | 21.15 [19.99, 21.59] | 10.46 | 10.31 | 35.61 | 0.990007 | 0.006083 |
| Q8 + BF16 text / 11 steps | 19.78 [19.55, 19.79] | 6.29 | 6.20 | 34.70 | 0.988382 | 0.006876 |
| Q8 + BF16 text / 12 steps | 21.08 [20.61, 21.45] | 6.22 | 6.15 | 35.83 | 0.991323 | 0.005321 |
| Q8 + Q8 text / 13 steps | 21.93 [21.93, 22.35] | 6.26 | 6.15 | 35.38 | 0.988748 | 0.005572 |

### poster_small: 640 × 640, seed 47191

[Image stack and complete prompt](../gallery/local/poster_small.md).

| Configuration | Median [min, max] s | Max physical GiB | Sampled tree GiB | PSNR dB | SSIM | LPIPS |
|---|---:|---:|---:|---:|---:|---:|
| MLX FP32 / 16 steps | 116.35 [116.04, 116.37] | 11.37 | 11.28 | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | 29.48 [29.45, 29.60] | 10.54 | 10.42 | 45.88 | 0.998724 | 0.000387 |
| Q8 + BF16 text / 16 steps | 28.06 [28.05, 28.19] | 6.22 | 6.19 | 32.30 | 0.984359 | 0.007120 |
| Q8 + Q8 text / 16 steps | 26.22 [26.20, 26.34] | 6.26 | 6.14 | 31.18 | 0.980651 | 0.009021 |
| Mixed 4/8 + Q8 text / 16 steps | 24.61 [24.60, 24.73] | 5.07 | 4.98 | 20.74 | 0.864732 | 0.118452 |
| Q4 + Q8 text / 16 steps | 23.96 [23.83, 24.06] | 4.31 | 4.25 | 20.46 | 0.851336 | 0.139543 |
| BF16 / 11 steps / fast | 22.79 [22.34, 23.30] | 10.52 | 10.46 | 32.36 | 0.984739 | 0.012508 |
| Q8 + BF16 text / 11 steps | 21.68 [21.51, 27.67] | 6.30 | 6.23 | 31.20 | 0.978262 | 0.011131 |
| Q8 + BF16 text / 12 steps | 22.53 [22.31, 25.12] | 6.29 | 6.23 | 31.72 | 0.981418 | 0.009015 |
| Q8 + Q8 text / 13 steps | 24.33 [22.98, 24.35] | 6.26 | 6.22 | 31.02 | 0.979459 | 0.010323 |

### teapot_edit_small: 768 × 512, seed 8521

[Image stack and complete prompt](../gallery/local/teapot_edit_small.md).

| Configuration | Median [min, max] s | Max physical GiB | Sampled tree GiB | PSNR dB | SSIM | LPIPS |
|---|---:|---:|---:|---:|---:|---:|
| MLX FP32 / 16 steps | 199.59 [199.54, 199.87] | 12.98 | 12.83 | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | 47.61 [47.59, 48.01] | 12.47 | 12.26 | 60.64 | 0.999609 | 0.000049 |
| Q8 + BF16 text / 16 steps | 47.38 [47.29, 47.43] | 7.46 | 7.39 | 56.96 | 0.999237 | 0.000100 |
| Q8 + Q8 text / 16 steps | 45.35 [45.32, 45.47] | 7.43 | 7.36 | 57.10 | 0.999304 | 0.000101 |
| Mixed 4/8 + Q8 text / 16 steps | 43.35 [43.35, 43.42] | 6.07 | 6.04 | 42.17 | 0.996069 | 0.001398 |
| Q4 + Q8 text / 16 steps | 41.81 [41.81, 41.82] | 5.25 | 5.22 | 38.93 | 0.990490 | 0.004367 |
| BF16 / 11 steps / fast | 36.13 [35.05, 36.89] | 12.43 | 12.31 | 49.26 | 0.997362 | 0.000475 |
| Q8 + BF16 text / 11 steps | 35.54 [34.86, 37.36] | 7.33 | 7.33 | 49.27 | 0.997448 | 0.000473 |
| Q8 + BF16 text / 12 steps | 38.92 [37.86, 39.43] | 7.38 | 7.31 | 50.71 | 0.997524 | 0.000413 |
| Q8 + Q8 text / 13 steps | 39.82 [39.38, 40.73] | 7.32 | 7.32 | 50.66 | 0.997546 | 0.000427 |

## Stage timing

Selected local presets, median stage compute seconds. Weight loading and other launch overhead are included in total launch timing above, not in these compute-only columns. Separate medians need not sum to the median launch.

| Case | Preset | Text encode s | Reference encode s | Denoise s | VAE decode s |
|---|---|---:|---:|---:|---:|
| man_dog | MLX FP32 / 16 steps | 2.69 | 0.00 | 268.49 | 3.21 |
| man_dog | Q8 + BF16 text / 16 steps | 2.12 | 0.00 | 61.14 | 1.42 |
| man_dog | BF16 / 11 steps / fast | 2.17 | 0.00 | 45.30 | 1.48 |
| man_dog | Q8 + BF16 text / 11 steps | 2.17 | 0.00 | 45.26 | 1.47 |
| man_dog | Q8 + BF16 text / 12 steps | 2.14 | 0.00 | 49.35 | 1.52 |
| man_dog | Q8 + Q8 text / 13 steps | 1.26 | 0.00 | 53.14 | 1.46 |
| teapot_small | MLX FP32 / 16 steps | 2.34 | 0.00 | 98.08 | 1.18 |
| teapot_small | Q8 + BF16 text / 16 steps | 2.10 | 0.00 | 20.84 | 0.55 |
| teapot_small | BF16 / 11 steps / fast | 2.11 | 0.00 | 14.79 | 0.66 |
| teapot_small | Q8 + BF16 text / 11 steps | 2.14 | 0.00 | 15.01 | 0.58 |
| teapot_small | Q8 + BF16 text / 12 steps | 1.99 | 0.00 | 16.59 | 0.57 |
| teapot_small | Q8 + Q8 text / 13 steps | 1.26 | 0.00 | 18.58 | 0.61 |
| poster_small | MLX FP32 / 16 steps | 2.68 | 0.00 | 109.32 | 1.24 |
| poster_small | Q8 + BF16 text / 16 steps | 2.13 | 0.00 | 23.53 | 0.57 |
| poster_small | BF16 / 11 steps / fast | 2.18 | 0.00 | 16.60 | 0.57 |
| poster_small | Q8 + BF16 text / 11 steps | 2.18 | 0.00 | 16.82 | 0.59 |
| poster_small | Q8 + BF16 text / 12 steps | 2.01 | 0.00 | 18.60 | 0.59 |
| poster_small | Q8 + Q8 text / 13 steps | 1.24 | 0.00 | 20.73 | 0.59 |
| teapot_edit_small | MLX FP32 / 16 steps | 2.33 | 0.64 | 191.93 | 1.17 |
| teapot_edit_small | Q8 + BF16 text / 16 steps | 2.07 | 0.31 | 42.23 | 0.54 |
| teapot_edit_small | BF16 / 11 steps / fast | 2.13 | 0.37 | 29.00 | 0.54 |
| teapot_edit_small | Q8 + BF16 text / 11 steps | 2.14 | 0.33 | 30.25 | 0.61 |
| teapot_edit_small | Q8 + BF16 text / 12 steps | 2.09 | 0.33 | 33.84 | 0.56 |
| teapot_edit_small | Q8 + Q8 text / 13 steps | 1.22 | 0.33 | 36.36 | 0.56 |

## Independent FP32 alignment

The newly measured MLX FP32 images were compared with hash-locked official-code FP32-16 references using identical inputs. The largest RGB-channel difference is 1/255 in each case.

| Case | PSNR dB | SSIM | LPIPS |
|---|---:|---:|---:|
| man_dog | 79.31 | 0.99999823 | 0.000000326 |
| teapot_small | 87.12 | 0.99999909 | 0.000000106 |
| poster_small | 78.67 | 0.99999634 | 0.000000583 |
| teapot_edit_small | 89.93 | 0.99999950 | 0.000000074 |

During the 16-step suite, system-wide swap was 1244.75 MiB before the first run and 1244.38 MiB after the last; the largest per-run increase was 3.88 MiB. These are desktop-wide observations and cannot be attributed exclusively to the model.

Machine-readable measurements, per-stage times, sample ranges and image checksums are in [16-step results](../results/m5-32gb-16step.json) and [preset results](../results/m5-32gb-presets.json). [Final conclusions](../RESULTS.md) distinguish the local sample from archived 22-case validation.
