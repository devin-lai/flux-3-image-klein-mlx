# double_exposure_s1 — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category illustration; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-double_exposure_s1.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-bf16-anchor-16.png) | 34.25 | 0.982298 | 0.015245 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-bf16-11.png) | 41.93 | 0.988701 | 0.010701 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-q8-quality-11.png) | 39.40 | 0.984970 | 0.013763 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-q8-quality-12.png) | 40.92 | 0.989872 | 0.007882 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-q8-13.png) | 39.56 | 0.988805 | 0.008861 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-bf16-fused-11.png) | 41.96 | 0.988749 | 0.010682 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/double_exposure_s1-hybrid-q8-12-archived.png) | 43.49 | 0.992256 | 0.005952 |

## Prompt

Digital double-exposure portrait in a muted blue monochrome palette, framed as a square head-and-shoulders composition with visible 35mm film grain. Centered in the foreground, a young East Asian man in his twenties faces the camera directly, shown from the shoulders up with fair skin, short black hair, dark eyes, and a neutral closed mouth. He wears a plain dark crew-neck shirt that merges into the shadowed lower portion of the image, and a polished silver hoop earring hangs from his left ear. His face remains sharply defined beneath a larger translucent profile of the same man layered across it, facing left. The oversized profile rises above and extends beyond the frontal head, its forehead, nose, lips, chin, and swept-back hair rendered as pale blue silhouettes with feathered edges. The translucent profile overlaps the frontal face so that both sets of eyes, cheekbones, and strands of hair intersect through the center. Behind them, the double exposure dissolves into a hazy blue field containing indistinct cloud forms and fine tonal texture, with no hard horizon. Cool diffused light catches the bridge of the frontal nose and the rim of the silver hoop, while deep navy shadows gather around the outer edges. Fine scratches, dust specks, uneven exposure, and dense analog grain run across the entire frame.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
