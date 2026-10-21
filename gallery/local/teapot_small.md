# teapot_small — Current MacBook Pro 32 GiB

Ten configurations per case: FP32/BF16/Q8-quality/Q8/mixed/Q4 at 16 steps, plus finalized BF16-11, Q8-quality-11/12 and Q8-13. Same input and seed; reduced-step measurements are later rounds.

Canvas 768 × 512; seed **1937**; category photo; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/local-teapot_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| MLX FP32 / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_small-fp32.png) | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_small-bf16.png) | 56.57 | 0.999428 | 0.000115 |
| Q8 + BF16 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_small-q8-quality.png) | 37.25 | 0.994718 | 0.003419 |
| Q8 + Q8 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_small-q8.png) | 36.24 | 0.990315 | 0.004314 |
| Mixed 4/8 + Q8 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_small-mixed.png) | 29.65 | 0.969659 | 0.017307 |
| Q4 + Q8 text / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/teapot_small-q4.png) | 29.02 | 0.952869 | 0.027506 |
| BF16 / 11 steps / fast | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_small-bf16-11.png) | 35.61 | 0.990007 | 0.006083 |
| Q8 + BF16 text / 11 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_small-q8-quality-11.png) | 34.70 | 0.988382 | 0.006876 |
| Q8 + BF16 text / 12 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_small-q8-quality-12.png) | 35.83 | 0.991323 | 0.005321 |
| Q8 + Q8 text / 13 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/teapot_small-q8-13.png) | 35.38 | 0.988748 | 0.005572 |

## Prompt

A carefully composed horizontal studio photograph of a pale blue porcelain teapot on a walnut table, with the spout pointing to the left and its curved handle on the right. A small ivory tea cup stands in the foreground. Behind the cup is a rectangular cream tea tin with the clear dark green words "EARL GREY" on its front. Three sprigs of lavender lie diagonally across a folded linen napkin at the right edge of the table. Soft daylight from a large window on the left creates gentle shadows, realistic ceramic highlights and a calm, warm atmosphere. The background is a plain pale grey plaster wall, slightly out of focus. Eye-level product photography, natural colors, finely resolved textures, no additional objects.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
