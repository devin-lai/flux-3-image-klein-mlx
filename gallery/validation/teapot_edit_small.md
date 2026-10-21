# teapot_edit_small — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 768 × 512; seed **8521**; category edit; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-teapot_edit_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-official-fp32-16.png) | reference | reference | reference |
| Official-policy BF16 on MPS / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-bf16-anchor-16.png) | 54.77 | 0.998603 | 0.000205 |
| BF16 / 11 steps / fast | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-bf16-11.png) | 49.23 | 0.997342 | 0.000481 |
| Q8 + BF16 text / 11 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-q8-quality-11.png) | 49.22 | 0.997434 | 0.000480 |
| Q8 + BF16 text / 12 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-q8-quality-12.png) | 50.66 | 0.997524 | 0.000421 |
| Q8 + Q8 text / 13 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-q8-13.png) | 50.60 | 0.997547 | 0.000433 |
| BF16 / 11 steps / fused | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-bf16-fused-11.png) | 49.22 | 0.997340 | 0.000466 |
| Hybrid Q8 / 12 steps / archived | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_edit_small-hybrid-q8-12-archived.png) | 49.99 | 0.997437 | 0.000428 |

## Prompt

The same carefully composed horizontal studio photograph of the teapot, cup, tea tin, lavender and linen napkin on the walnut table shown in the reference image. The porcelain teapot is now a deep glossy red, with its original shape, spout pointing left and curved handle on the right. Keep the ivory cup in the foreground, the cream tea tin with the dark green words "EARL GREY" behind the cup, and the three lavender sprigs across the linen napkin on the right. Preserve the camera angle, object positions, pale grey plaster background, soft daylight from the left, realistic highlights and warm natural color palette. Only the teapot glaze changes from pale blue to deep red.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/teapot_edit_small-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
