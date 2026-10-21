# still_life_wide — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1248 × 832; seed **1**; category photo; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-still_life_wide.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-bf16-anchor-16.png) | 25.04 | 0.938084 | 0.059140 |
| BF16 / 11 steps / fast | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-bf16-11.png) | 33.61 | 0.984618 | 0.010025 |
| Q8 + BF16 text / 11 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-q8-quality-11.png) | 31.10 | 0.976898 | 0.016329 |
| Q8 + BF16 text / 12 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-q8-quality-12.png) | 31.84 | 0.980886 | 0.012070 |
| Q8 + Q8 text / 13 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-q8-13.png) | 26.65 | 0.957516 | 0.036455 |
| BF16 / 11 steps / fused | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-bf16-fused-11.png) | 34.27 | 0.985297 | 0.009446 |
| Hybrid Q8 / 12 steps / archived | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/still_life_wide-hybrid-q8-12-archived.png) | 27.24 | 0.962903 | 0.032509 |

## Prompt

Large-format still-life photograph in the register of a Dutch painting, composed vertically on a dark oak table against a deep black background. A single hard window light enters from the left, illuminating the objects with warm highlights and leaving their right sides in dense brown-black shadow. In the upper center, a torn rustic loaf rests off-center on the tabletop, its rough golden-brown crust split open to reveal an irregular pale crumb; several crumbs lie scattered below it. On the left stands a heavy pewter jug with a rounded body, narrow neck, curved handle, and dull silver surface marked by tarnish and small dents. The jug catches a bright vertical reflection along its left rim while its base disappears into shadow. Across the lower center sit exactly three lemons: two whole yellow lemons near the front and one peeled lemon beside them, its exposed flesh curling outward in a broad spiral peel. The remaining whole lemons have dimpled rinds and short shadows cast toward the right. A long old iron knife lies diagonally across the foreground, its blade pointing toward the peeled lemon and its worn wooden handle extending toward the lower right. The dark oak planks show pronounced grain, shallow scratches, and a narrow seam beneath the arrangement. The composition has restrained earth tones, concentrated chiaroscuro, crisp detail on the illuminated food and metal, and broad areas of unbroken darkness above and around the still life.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
