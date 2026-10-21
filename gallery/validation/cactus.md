# cactus — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **1**; category edit; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-cactus.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-bf16-anchor-16.png) | 53.92 | 0.998671 | 0.000295 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-bf16-11.png) | 46.93 | 0.997152 | 0.001005 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-q8-quality-11.png) | 46.43 | 0.997114 | 0.001070 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-q8-quality-12.png) | 49.54 | 0.997471 | 0.000830 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-q8-13.png) | 49.73 | 0.997525 | 0.000800 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-bf16-fused-11.png) | 46.93 | 0.997154 | 0.001002 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cactus-hybrid-q8-12-archived.png) | 49.46 | 0.997410 | 0.000838 |

## Prompt

Add a small potted cactus <obj_1> on the wooden tabletop in the lower-right area indicated by the locked placement box, with its pot resting near the lower-right edge of the white coffee mug <mug_1>. Give it a compact green cactus in a simple terracotta pot, matching the scene’s perspective, warm sunlight, and natural contact shadow. Keep the coffee mug and every other part of the image unchanged. [{"id": "obj_1", "from": "target", "src_bbox": null, "tgt_bbox": [550, 620, 850, 850], "desc": "A small potted cactus with a compact upright green barrel cactus featuring several short vertical ribs and evenly spaced clusters of rounded spines, planted in dark soil inside a simple unadorned terracotta pot with a slightly flared rim."}, {"id": "mug_1", "from": "ref_image_0", "src_bbox": [354, 283, 768, 755], "tgt_bbox": [354, 283, 768, 755], "desc": "A large plain white ceramic coffee mug with a rounded body and broad curved handle, filled with dark black coffee and a thin ring of steam rising above the rim."}]

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/coffee-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
