# Select a model and preset

Start with **Q8 quality at 16 steps** for a general choice, or **Q8 quality at 11 steps** when latency matters. Choose using the original image stacks as well as the aggregate metrics. [Run a preset](USAGE.md) with `--preset` and the exact name below.

| Preset | Model components | Local time | Peak physical memory | Use |
|---|---|---:|---:|---|
| `q8-quality-16` | Q8 transformer + BF16 text | 38.75 s | 7.46 GiB | Default quality/storage compromise |
| `q8-quality-11` | Q8 transformer + BF16 text | 29.69 s | 7.33 GiB | Fastest reduced-step preset tested locally |
| `q8-quality-12` | Q8 transformer + BF16 text | 31.70 s | 7.38 GiB | Closer FP32-16 agreement than the 11-step preset |
| `q8-16` | Q8 transformer + Q8 text | 36.65 s | 7.43 GiB | Smaller text-model download |
| `q8-13` | Q8 transformer + Q8 text | 33.34 s | 7.32 GiB | Validated reduced-step option with Q8 text |
| `bf16-16` | BF16 transformer + BF16 text | 40.34 s | 12.47 GiB | Highest-fidelity unquantized control |
| `bf16-11` | BF16 transformer + BF16 text | 30.99 s | 12.43 GiB | Reduced steps with unquantized weights |
| `mixed-16` | Mixed 4/8-bit transformer + Q8 text | 34.91 s | 6.07 GiB | Lower memory; larger visual changes |
| `q4-16` | Q4 transformer + Q8 text | 33.75 s | 5.53 GiB | Lowest memory; stronger fidelity tradeoffs |

Times are geometric means of four per-case median latencies, each measured three times on the M5/32 GiB Mac. Memory is the maximum measured physical footprint. Reduced-step results and 16-step results were collected in separate rounds. The FP32-16 control measured **161.16 s** and **12.98 GiB**. Full ranges, arithmetic details and PSNR/SSIM/LPIPS are in the [test report](reports/macbook-pro-32gb.md).

| Inspect the result | Image stack |
|---|---|
| Photo, textures and anatomy | [Man and dog](gallery/local/man_dog.md) |
| Product composition and fine geometry | [Teapot](gallery/local/teapot_small.md) |
| Legible text and exact object counts | [Typography](gallery/local/poster_small.md) |
| Reference preservation and requested color edit | [Image editing](gallery/local/teapot_edit_small.md) |
| Broader 22-case confirmation and historical previews | [Complete gallery](gallery/README.md) |

The Q4 typography sample adds a second pencil. Mixed/Q4 remain memory-oriented options; they did not pass the stricter full-set fidelity criterion used to select the reduced-step quality presets. [Final conclusions](RESULTS.md) distinguish measured advantages from limits of the tested prompts and schedules.
