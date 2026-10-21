# poster_small — Current MacBook Pro 32 GiB

Ten configurations per case: FP32/BF16/Q8-quality/Q8/mixed/Q4 at 16 steps, plus finalized BF16-11, Q8-quality-11/12 and Q8-13. Same input and seed; reduced-step measurements are later rounds.

Canvas 640 × 640; seed **47191**; category typography; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/local-poster_small.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| MLX FP32 / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/poster_small-fp32.png) | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/poster_small-bf16.png) | 45.88 | 0.998724 | 0.000387 |
| Q8 + BF16 text / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/poster_small-q8-quality.png) | 32.30 | 0.984359 | 0.007120 |
| Q8 + Q8 text / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/poster_small-q8.png) | 31.18 | 0.980651 | 0.009021 |
| Mixed 4/8 + Q8 text / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/poster_small-mixed.png) | 20.74 | 0.864732 | 0.118452 |
| Q4 + Q8 text / 16 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/poster_small-q4.png) | 20.46 | 0.851336 | 0.139543 |
| BF16 / 11 steps / fast | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/poster_small-bf16-11.png) | 32.36 | 0.984739 | 0.012508 |
| Q8 + BF16 text / 11 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/poster_small-q8-quality-11.png) | 31.20 | 0.978262 | 0.011131 |
| Q8 + BF16 text / 12 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/poster_small-q8-quality-12.png) | 31.72 | 0.981418 | 0.009015 |
| Q8 + Q8 text / 13 steps | [Original 640 × 640 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/poster_small-q8-13.png) | 31.02 | 0.979459 | 0.010323 |

## Prompt

An editorial still-life photograph in a quiet artist's studio, with a square composition and realistic fine material detail. A large cream paper poster leans against a pale sage wall in the upper center of the frame. The poster reads "MORNING LIGHT" in two lines of dark navy serif lettering, with "STUDIO 27" printed in small widely spaced capitals beneath it. The lettering is clean and legible, surrounded by ample blank paper.

On a warm oak table in front of the poster sits a low cobalt blue ceramic bowl containing three yellow lemons, one with a small green leaf attached. A clear ribbed glass of water stands on the right, casting a delicate caustic pattern across the wood. A loosely folded ivory linen cloth lies on the left, with individual woven fibers visible along its edge. A sharpened red pencil rests diagonally beside the cloth.

Soft morning sunlight enters from a window outside the upper left of the image, forming long gentle shadows toward the lower right. The paper has a subtle matte texture, the bowl has a slightly uneven glazed rim, and the oak grain runs horizontally. The camera is at table height with a normal lens and enough depth of field to keep the poster lettering and foreground objects in focus. Natural muted color grading, no people, no additional objects or text.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
