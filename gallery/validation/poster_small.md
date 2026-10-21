# poster_small — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 640 × 640; seed **47191**; category typography; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-poster_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-official-fp32-16.png) | reference | reference | reference |
| Official-policy BF16 on MPS / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-bf16-anchor-16.png) | 25.62 | 0.956727 | 0.019896 |
| BF16 / 11 steps / fast | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-bf16-11.png) | 32.14 | 0.984156 | 0.013037 |
| Q8 + BF16 text / 11 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-q8-quality-11.png) | 31.33 | 0.978587 | 0.011048 |
| Q8 + BF16 text / 12 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-q8-quality-12.png) | 31.84 | 0.981622 | 0.009065 |
| Q8 + Q8 text / 13 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-q8-13.png) | 30.94 | 0.979138 | 0.010418 |
| BF16 / 11 steps / fused | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-bf16-fused-11.png) | 32.59 | 0.985019 | 0.012311 |
| Hybrid Q8 / 12 steps / archived | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/poster_small-hybrid-q8-12-archived.png) | 33.00 | 0.983137 | 0.008436 |

## Prompt

An editorial still-life photograph in a quiet artist's studio, with a square composition and realistic fine material detail. A large cream paper poster leans against a pale sage wall in the upper center of the frame. The poster reads "MORNING LIGHT" in two lines of dark navy serif lettering, with "STUDIO 27" printed in small widely spaced capitals beneath it. The lettering is clean and legible, surrounded by ample blank paper.

On a warm oak table in front of the poster sits a low cobalt blue ceramic bowl containing three yellow lemons, one with a small green leaf attached. A clear ribbed glass of water stands on the right, casting a delicate caustic pattern across the wood. A loosely folded ivory linen cloth lies on the left, with individual woven fibers visible along its edge. A sharpened red pencil rests diagonally beside the cloth.

Soft morning sunlight enters from a window outside the upper left of the image, forming long gentle shadows toward the lower right. The paper has a subtle matte texture, the bowl has a slightly uneven glazed rim, and the oak grain runs horizontally. The camera is at table height with a normal lens and enough depth of field to keep the poster lettering and foreground objects in focus. Natural muted color grading, no people, no additional objects or text.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
