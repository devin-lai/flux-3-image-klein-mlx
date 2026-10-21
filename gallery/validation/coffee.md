# coffee — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **21**; category edit; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-coffee.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-bf16-anchor-16.png) | 44.72 | 0.997307 | 0.001667 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-bf16-11.png) | 42.85 | 0.995808 | 0.002017 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-q8-quality-11.png) | 42.35 | 0.995686 | 0.002058 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-q8-quality-12.png) | 44.58 | 0.996498 | 0.001415 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-q8-13.png) | 41.01 | 0.994016 | 0.003446 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-bf16-fused-11.png) | 42.95 | 0.995850 | 0.001989 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/coffee-hybrid-q8-12-archived.png) | 41.08 | 0.994018 | 0.003428 |

## Prompt

Create a photograph preserving the first image exactly as the canvas: keep the same close, slightly elevated camera position, the white ceramic mug in the same place on the worn honey-brown wooden tabletop, the window directly behind it, the cream curtain at frame-left, the white-painted window frame with its small chips and weathering, and the blue-green outdoor foliage visible through the glass. Keep the same warm sunlight entering from frame-right, the long diagonal mug shadow across the tabletop, the window reflections, and every scratch, seam, and mark in the wood. Fill the mug completely with dark brown coffee, with the liquid surface sitting just below the rim and the existing wisps of steam rising naturally above it. Add one golden-brown croissant beside the mug at frame-right, resting directly on the tabletop near the handle without covering it. Give the croissant its familiar curved, flaky layered form, with a few loose pastry flakes nearby. Match its scale and perspective to the mug, with warm highlights along its upper ridges and a soft contact shadow falling toward frame-left, consistent with the existing sunlight.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/coffee-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
