# balloons — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **1**; category layout; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-balloons.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-bf16-anchor-16.png) | 39.62 | 0.995172 | 0.002805 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-bf16-11.png) | 37.27 | 0.983954 | 0.011567 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-q8-quality-11.png) | 37.09 | 0.983255 | 0.012045 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-q8-quality-12.png) | 40.37 | 0.990020 | 0.005173 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-q8-13.png) | 43.39 | 0.993265 | 0.003466 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-bf16-fused-11.png) | 37.29 | 0.984000 | 0.011531 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/balloons-hybrid-q8-12-archived.png) | 41.31 | 0.991281 | 0.004730 |

## Prompt

Full-color outdoor photograph at sunrise, with a broad dawn sky <sky_1> above a green valley <valley_1>. On the left, a large hot-air balloon <obj_1> floats over the valley, while a smaller blue hot-air balloon <obj_2> hangs farther back on the right. Along the horizon, the rising sun <sun_1> appears between distant mountain ridges <mountain_1>, casting low orange light across the slopes and leaving the foreground meadow in cooler shadow. [{"id": "obj_1", "bbox": [80, 60, 480, 380], "desc": "A large red and yellow striped hot-air balloon with alternating vertical fabric panels, a rounded envelope, dark suspension cables, and a small rectangular wicker basket hanging below; the lower edge of the envelope is partly shaded by the sunrise angle."}, {"id": "obj_2", "bbox": [200, 620, 420, 800], "desc": "A small blue hot-air balloon with a rounded cobalt-blue envelope, narrow darker seams, fine suspension lines, and a tiny brown basket."}, {"id": "sky_1", "bbox": [0, 0, 650, 1000], "desc": "A clear sunrise sky grading from pale orange near the horizon through peach to muted blue overhead, with several thin horizontal clouds catching warm light."}, {"id": "sun_1", "bbox": [470, 455, 535, 525], "desc": "A low circular sunrise disk in bright yellow-orange, partially veiled by the distant ridge line."}, {"id": "mountain_1", "bbox": [430, 0, 690, 1000], "desc": "Layered distant mountain ridges forming an uneven horizon, with blue-gray silhouettes in front and warmer brown-green slopes along their upper edges."}, {"id": "valley_1", "bbox": [560, 0, 1000, 1000], "desc": "A broad green valley with rolling grassy slopes, scattered darker tree masses, and a winding river reflecting a narrow strip of orange morning light; the nearest meadow contains patches of deep green shadow and uneven vegetation."}]

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
