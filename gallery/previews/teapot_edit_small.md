# teapot_edit_small — Archived previews

Earlier 6/8-step results. Reference is FP32 at 8 steps; images are archived repeat means, with older runtime settings. Previous Q8/Q4 weights are not shipped.

Canvas 768 × 512; seed **8521**; category edit; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/previews-teapot_edit_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official FP32 / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-official-fp32-8.png) | ∞ | 1.000000 | not measured |
| Previous 8-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-previous-q8-8.png) | 51.02 | 0.997847 | not measured |
| Previous 4-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-previous-q4-8.png) | 35.80 | 0.983376 | not measured |
| 8-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-q8-8.png) | 56.46 | 0.999030 | not measured |
| 4-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-q4-8.png) | 38.61 | 0.990404 | not measured |
| Mixed 4/8-bit / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-mixed-8.png) | 42.74 | 0.996017 | not measured |
| BF16 control / 8 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-bf16-8.png) | 60.41 | 0.999576 | not measured |
| Mixed 4/8-bit / 6 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/teapot_edit_small-mixed-6.png) | 42.82 | 0.994695 | not measured |

## Prompt

The same carefully composed horizontal studio photograph of the teapot, cup, tea tin, lavender and linen napkin on the walnut table shown in the reference image. The porcelain teapot is now a deep glossy red, with its original shape, spout pointing left and curved handle on the right. Keep the ivory cup in the foreground, the cream tea tin with the dark green words "EARL GREY" behind the cup, and the three lavender sprigs across the linen napkin on the right. Preserve the camera angle, object positions, pale grey plaster background, soft daylight from the left, realistic highlights and warm natural color palette. Only the teapot glaze changes from pale blue to deep red.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/teapot_edit_small-0.png)

Scores in this page are relative to the archived FP32-8 repeat mean. The images were produced with the recorded earlier inputs; the case prompt above is shared with the current suite.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
