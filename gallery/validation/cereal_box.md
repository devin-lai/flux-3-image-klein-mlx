# cereal_box — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category typography; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-cereal_box.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-bf16-anchor-16.png) | 29.48 | 0.977618 | 0.010088 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-bf16-11.png) | 31.09 | 0.978920 | 0.008386 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-q8-quality-11.png) | 30.84 | 0.977894 | 0.008902 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-q8-quality-12.png) | 34.37 | 0.988153 | 0.004311 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-q8-13.png) | 35.26 | 0.990370 | 0.003131 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-bf16-fused-11.png) | 31.08 | 0.978883 | 0.008461 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/cereal_box-hybrid-q8-12-archived.png) | 34.41 | 0.988504 | 0.003960 |

## Prompt

Studio product photograph, shot straight-on with flat, even lighting and a deep depth of field, showing a single 1960s cereal box centered against a plain warm cream background. The rectangular cardboard box fills most of the frame, its front panel facing the camera squarely with crisp edges and no perspective distortion. The package uses flat screen-printed colors in mustard yellow, burnt orange, sky blue, cream, and dark brown, with minor ink texture along the printed shapes. Across the top, large bold rounded letters read "MORNING OATS" in dark brown on a pale yellow header band. Directly below, a curved red banner carries the white lowercase text "with real honey". In the center, a friendly cartoon bear with round ears, a tan muzzle, black oval eyes, and a simple smiling mouth stands behind a small breakfast bowl, holding a long silver spoon upright in one paw. The spoon rises above the bowl beside the bear’s head. Curving script across the lower middle reads "A good start to the day" in dark blue cursive lettering. Small illustrated oat stalks and three golden honey droplets decorate the sides without covering the main wording. At the bottom right corner, compact uppercase sans-serif text reads "NET WT 16 OZ". A narrow cream border encloses the entire front design, with worn corners and a few tiny scuffs on the cardboard surface.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
