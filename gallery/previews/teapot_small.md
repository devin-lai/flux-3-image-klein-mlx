# teapot_small — Archived previews

Earlier 6/8-step results. Reference is FP32 at 8 steps; images are archived repeat means, with older runtime settings. Previous Q8/Q4 weights are not shipped.

Canvas 768 × 512; seed **1937**; category photo; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/previews-teapot_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official FP32 / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-official-fp32-8.png) | ∞ | 1.000000 | not measured |
| Previous 8-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-previous-q8-8.png) | 36.27 | 0.988893 | not measured |
| Previous 4-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-previous-q4-8.png) | 22.61 | 0.836463 | not measured |
| 8-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-q8-8.png) | 37.75 | 0.989775 | not measured |
| 4-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-q4-8.png) | 29.24 | 0.946049 | not measured |
| Mixed 4/8-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-mixed-8.png) | 30.83 | 0.962304 | not measured |
| BF16 control / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-bf16-8.png) | 55.84 | 0.999334 | not measured |
| Mixed 4/8-bit / 6 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_small-mixed-6.png) | 26.66 | 0.910191 | not measured |

## Prompt

A carefully composed horizontal studio photograph of a pale blue porcelain teapot on a walnut table, with the spout pointing to the left and its curved handle on the right. A small ivory tea cup stands in the foreground. Behind the cup is a rectangular cream tea tin with the clear dark green words "EARL GREY" on its front. Three sprigs of lavender lie diagonally across a folded linen napkin at the right edge of the table. Soft daylight from a large window on the left creates gentle shadows, realistic ceramic highlights and a calm, warm atmosphere. The background is a plain pale grey plaster wall, slightly out of focus. Eye-level product photography, natural colors, finely resolved textures, no additional objects.

Scores in this page are relative to the archived FP32-8 repeat mean. The images were produced with the recorded earlier inputs; the case prompt above is shared with the current suite.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
