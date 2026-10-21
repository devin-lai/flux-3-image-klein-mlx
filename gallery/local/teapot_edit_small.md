# teapot_edit_small — Current MacBook Pro 32 GiB

Ten configurations per case: FP32/BF16/Q8-quality/Q8/mixed/Q4 at 16 steps, plus finalized BF16-11, Q8-quality-11/12 and Q8-13. Same input and seed; reduced-step measurements are later rounds.

Canvas 768 × 512; seed **8521**; category edit; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/local-teapot_edit_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| MLX FP32 / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_edit_small-fp32.png) | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_edit_small-bf16.png) | 60.64 | 0.999609 | 0.000049 |
| Q8 + BF16 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_edit_small-q8-quality.png) | 56.96 | 0.999237 | 0.000100 |
| Q8 + Q8 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_edit_small-q8.png) | 57.10 | 0.999304 | 0.000101 |
| Mixed 4/8 + Q8 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_edit_small-mixed.png) | 42.17 | 0.996069 | 0.001398 |
| Q4 + Q8 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_edit_small-q4.png) | 38.93 | 0.990490 | 0.004367 |
| BF16 / 11 steps / fast | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_edit_small-bf16-11.png) | 49.26 | 0.997362 | 0.000475 |
| Q8 + BF16 text / 11 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_edit_small-q8-quality-11.png) | 49.27 | 0.997448 | 0.000473 |
| Q8 + BF16 text / 12 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_edit_small-q8-quality-12.png) | 50.71 | 0.997524 | 0.000413 |
| Q8 + Q8 text / 13 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_edit_small-q8-13.png) | 50.66 | 0.997546 | 0.000427 |

## Prompt

The same carefully composed horizontal studio photograph of the teapot, cup, tea tin, lavender and linen napkin on the walnut table shown in the reference image. The porcelain teapot is now a deep glossy red, with its original shape, spout pointing left and curved handle on the right. Keep the ivory cup in the foreground, the cream tea tin with the dark green words "EARL GREY" behind the cup, and the three lavender sprigs across the linen napkin on the right. Preserve the camera angle, object positions, pale grey plaster background, soft daylight from the left, realistic highlights and warm natural color palette. Only the teapot glaze changes from pale blue to deep red.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/teapot_edit_small-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
