# teapot_small — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 768 × 512; seed **1937**; category photo; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-teapot_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-official-fp32-16.png) | reference | reference | reference |
| Official-policy BF16 on MPS / 16 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/teapot_edit_small-0.png) | 34.54 | 0.990254 | 0.006332 |
| BF16 / 11 steps / fast | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-bf16-11.png) | 35.56 | 0.989890 | 0.006146 |
| Q8 + BF16 text / 11 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-q8-quality-11.png) | 34.66 | 0.988283 | 0.006970 |
| Q8 + BF16 text / 12 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-q8-quality-12.png) | 35.81 | 0.991265 | 0.005349 |
| Q8 + Q8 text / 13 steps | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-q8-13.png) | 35.41 | 0.988777 | 0.005563 |
| BF16 / 11 steps / fused | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-bf16-fused-11.png) | 35.55 | 0.989847 | 0.006184 |
| Hybrid Q8 / 12 steps / archived | [Original 768 × 512 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/teapot_small-hybrid-q8-12-archived.png) | 36.57 | 0.991837 | 0.005202 |

## Prompt

A carefully composed horizontal studio photograph of a pale blue porcelain teapot on a walnut table, with the spout pointing to the left and its curved handle on the right. A small ivory tea cup stands in the foreground. Behind the cup is a rectangular cream tea tin with the clear dark green words "EARL GREY" on its front. Three sprigs of lavender lie diagonally across a folded linen napkin at the right edge of the table. Soft daylight from a large window on the left creates gentle shadows, realistic ceramic highlights and a calm, warm atmosphere. The background is a plain pale grey plaster wall, slightly out of focus. Eye-level product photography, natural colors, finely resolved textures, no additional objects.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
