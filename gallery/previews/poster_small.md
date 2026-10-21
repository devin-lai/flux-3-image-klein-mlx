# poster_small — Archived previews

Earlier 6/8-step results. Reference is FP32 at 8 steps; images are archived repeat means, with older runtime settings. Previous Q8/Q4 weights are not shipped.

Canvas 640 × 640; seed **47191**; category typography; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/previews-poster_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official FP32 / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-official-fp32-8.png) | ∞ | 1.000000 | not measured |
| Previous 8-bit / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-previous-q8-8.png) | 26.62 | 0.940932 | not measured |
| Previous 4-bit / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-previous-q4-8.png) | 20.42 | 0.789526 | not measured |
| 8-bit / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-q8-8.png) | 29.21 | 0.968953 | not measured |
| 4-bit / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-q4-8.png) | 23.02 | 0.881681 | not measured |
| Mixed 4/8-bit / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-mixed-8.png) | 23.29 | 0.882768 | not measured |
| BF16 control / 8 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-bf16-8.png) | 27.53 | 0.952900 | not measured |
| Mixed 4/8-bit / 6 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/poster_small-mixed-6.png) | 23.08 | 0.877338 | not measured |

## Prompt

An editorial still-life photograph in a quiet artist's studio, with a square composition and realistic fine material detail. A large cream paper poster leans against a pale sage wall in the upper center of the frame. The poster reads "MORNING LIGHT" in two lines of dark navy serif lettering, with "STUDIO 27" printed in small widely spaced capitals beneath it. The lettering is clean and legible, surrounded by ample blank paper.

On a warm oak table in front of the poster sits a low cobalt blue ceramic bowl containing three yellow lemons, one with a small green leaf attached. A clear ribbed glass of water stands on the right, casting a delicate caustic pattern across the wood. A loosely folded ivory linen cloth lies on the left, with individual woven fibers visible along its edge. A sharpened red pencil rests diagonally beside the cloth.

Soft morning sunlight enters from a window outside the upper left of the image, forming long gentle shadows toward the lower right. The paper has a subtle matte texture, the bowl has a slightly uneven glazed rim, and the oak grain runs horizontally. The camera is at table height with a normal lens and enough depth of field to keep the poster lettering and foreground objects in focus. Natural muted color grading, no people, no additional objects or text.

Scores in this page are relative to the archived FP32-8 repeat mean. The images were produced with the recorded earlier inputs; the case prompt above is shared with the current suite.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
