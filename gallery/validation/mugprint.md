# mugprint — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **23**; category multi-edit; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-mugprint.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-bf16-anchor-16.png) | 54.00 | 0.998481 | 0.000322 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-bf16-11.png) | 51.14 | 0.997579 | 0.000580 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-q8-quality-11.png) | 50.28 | 0.997317 | 0.000677 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-q8-quality-12.png) | 50.35 | 0.997279 | 0.000739 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-q8-13.png) | 49.30 | 0.996844 | 0.000797 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-bf16-fused-11.png) | 51.16 | 0.997586 | 0.000580 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/mugprint-hybrid-q8-12-archived.png) | 50.69 | 0.997381 | 0.000692 |

## Prompt

Create a photograph preserving the first image exactly as the canvas: keep the white ceramic mug filled with dark coffee in the same position on the worn honey-brown wooden tabletop, with its handle pointing toward frame-right, the window directly behind it, the off-white curtain at frame-left, the weathered white window frame, the blue sky and green foliage visible through the glass, and the same low sunlight casting the mug’s long angular shadow across the table. Print the golden retriever from the second image onto the front of the mug as a centered ceramic decal, replacing only the plain white surface of the mug’s body. Depict the dog’s seated, near-frontal portrait from the second image, including its golden coat, wet-looking fur, dark eyes, black nose, floppy ears, and calm expression, but omit the beach, ocean, and cloudy sky from the printed image. Scale the dog to fit naturally within the mug’s visible front face, following the mug’s curved surface with correct perspective and subtle distortion. Integrate the print into the ceramic glaze so it follows the rounded contours, with the existing sunlight and shadow falling naturally across it. Leave every other element unchanged.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/coffee-0.png)

[Reference input 2](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/bandana-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
