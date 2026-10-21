# bandana — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **22**; category edit; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-bandana.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-bf16-anchor-16.png) | 54.65 | 0.998529 | 0.000333 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-bf16-11.png) | 44.26 | 0.996430 | 0.001706 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-q8-quality-11.png) | 44.12 | 0.996349 | 0.001789 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-q8-quality-12.png) | 43.96 | 0.996571 | 0.002477 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-q8-13.png) | 47.96 | 0.997560 | 0.000851 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-bf16-fused-11.png) | 44.35 | 0.996455 | 0.001642 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/bandana-hybrid-q8-12-archived.png) | 45.88 | 0.996994 | 0.001233 |

## Prompt

Create a photograph preserving the first image exactly as the canvas: keep the same golden retriever seated in the same position on the broad beach, with its body facing forward, front paws planted in the sand, head held near-frontally, and eyes looking directly toward the camera. Preserve the dog’s golden coat, wet fur, floppy ears, dark eyes, black nose, facial markings, and calm expression without alteration. Add a red triangular bandana tied securely around the dog’s neck, with the knot centered beneath its chin and the two pointed ends resting naturally over the wet chest fur. The bandana is solid red fabric with subtle woven texture, following the contours of the neck and sitting partly over the golden fur, with natural folds, contact shadows, and dampness consistent with the beach setting. Keep unchanged the pale gray sand scattered with small shells and footprints, the dog’s paw impressions, the calm gray-blue ocean with low waves, the distant horizon, and the expansive layered gray storm clouds with the narrow blue opening near the horizon. Preserve the original eye-level camera position, square composition, subdued overcast daylight, colors, perspective, and every other background detail exactly as photographed.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/bandana-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
