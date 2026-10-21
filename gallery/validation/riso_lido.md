# riso_lido — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category illustration; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-riso_lido.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-bf16-anchor-16.png) | 23.97 | 0.934764 | 0.045469 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-bf16-11.png) | 27.46 | 0.961365 | 0.022850 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-q8-quality-11.png) | 23.92 | 0.925722 | 0.049028 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-q8-quality-12.png) | 24.00 | 0.931311 | 0.046685 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-q8-13.png) | 21.64 | 0.891685 | 0.077112 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-bf16-fused-11.png) | 27.84 | 0.963094 | 0.020925 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/riso_lido-hybrid-q8-12-archived.png) | 28.64 | 0.968822 | 0.016262 |

## Prompt

Two-ink risograph poster printed in fluorescent orange and blue on warm off-white paper, with coarse halftone grain, uneven ink coverage, and visible color misregistration along the edges of every shape. A swimmer dominates the upper center, captured mid-dive headfirst toward the lower left, body stretched diagonally into a long streamlined pose. The swimmer is constructed from flat geometric shapes: a fluorescent orange head and torso, blue limbs, and a blue cap with an orange face opening. One arm reaches forward while the other follows close behind, and the legs trail together above the waterline. Broad blue wave bands sweep across the middle as angular horizontal forms, interrupted by fluorescent orange circles and sharp splash shapes around the diver. Behind the swimmer, a large fluorescent orange sun sits near the top edge against a blue field, with offset orange contours creating narrow doubled outlines. At the bottom, the word "LIDO" spans nearly the full width in oversized uppercase block letters, alternating between fluorescent orange and blue with misregistered edges. The composition contains only the swimmer, abstract water, sun, and the single word "LIDO", with no additional lettering, numbers, logos, or symbols.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
