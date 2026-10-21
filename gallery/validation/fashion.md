# fashion — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category photo; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-fashion.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-bf16-anchor-16.png) | 40.15 | 0.994177 | 0.002070 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-bf16-11.png) | 40.45 | 0.993241 | 0.003131 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-q8-quality-11.png) | 38.19 | 0.991555 | 0.004251 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-q8-quality-12.png) | 38.85 | 0.992409 | 0.003664 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-q8-13.png) | 38.40 | 0.992345 | 0.003633 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-bf16-fused-11.png) | 40.65 | 0.993407 | 0.003089 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/fashion-hybrid-q8-12-archived.png) | 42.60 | 0.994619 | 0.002427 |

## Prompt

Studio fashion photograph captured on a Hasselblad medium-format camera, full-length portrait against an unmarked mustard seamless paper backdrop. A Black female model in her twenties with dark skin and a tall, slender build stands just left of center, facing the camera with her body turned a few degrees toward frame-left. Her short natural hair is cropped close to the head, leaving the oversized grey wool coat as the dominant form. The heavy coat falls below her knees in broad, boxy folds, with dropped shoulders, wide sleeves, a high folded collar, concealed front closure, and two deep patch pockets. Both hands are tucked into the pockets, pulling the lower front into angular pleats. Her face has a neutral expression, closed lips, and a direct gaze. One hard key light from the upper left strikes her forehead, cheek, shoulder, and the raised ridges of the wool, producing bright highlights along the left side while the right side falls into dense charcoal-grey shade. A crisp-edged shadow extends behind her across the mustard paper toward the lower right, following the silhouette of the coat and legs. Dark straight trousers and black leather ankle boots emerge beneath the hem. The seamless paper curves into the floor without a horizon line, its matte surface showing fine tonal falloff around the sharp cast shadow. The composition contains only the model, coat, footwear, mustard background, and shadow, with clean negative space above and to the right.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
