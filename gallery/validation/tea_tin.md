# tea_tin — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **1**; category typography; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-tea_tin.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-bf16-anchor-16.png) | 28.39 | 0.967521 | 0.022575 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-bf16-11.png) | 38.54 | 0.994199 | 0.002987 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-q8-quality-11.png) | 38.43 | 0.994127 | 0.003004 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-q8-quality-12.png) | 41.26 | 0.995854 | 0.002005 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-q8-13.png) | 34.70 | 0.989941 | 0.005697 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-bf16-fused-11.png) | 38.54 | 0.994218 | 0.002969 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/tea_tin-hybrid-q8-12-archived.png) | 36.44 | 0.991739 | 0.005464 |

## Prompt

Studio product photograph of a cylindrical tea tin against a seamless warm grey background, shot from a slightly elevated three-quarter angle with hard side light entering from the left. The tin stands upright in the center, its front facing the viewer and its right side receding into shadow. Its body is coated in dark green enamel with a narrow gold rim around the top and bottom edges. A fitted dark green lid sits flush above the body, edged by a thin gold band; the raised metal lid knob catches a bright highlight while the right half falls into deep shade. Across the upper front, large embossed gold serif capitals read "HIGHLAND BREAKFAST". Directly beneath, smaller gold lettering reads "Assam and Ceylon leaf". Below it, a circular gold roundel contains the text "est. 1884" in compact dark green type. On the visible right side of the tin, small white sans-serif lettering follows the curve of the cylinder and reads "Brew for four minutes. One spoon per cup and one for the pot." The hard light creates a sharp vertical highlight along the left edge, reveals the enamel’s smooth reflective surface, and casts a dense shadow behind and to the right of the tin. A few tiny scuffs interrupt the green finish near the lower rim, and the tin rests on a matte tabletop with a short, crisp cast shadow extending toward the lower right.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
