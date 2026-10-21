# church — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category architecture; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-church.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-bf16-anchor-16.png) | 36.33 | 0.981058 | 0.012686 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-bf16-11.png) | 40.28 | 0.986654 | 0.013391 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-q8-quality-11.png) | 39.81 | 0.986460 | 0.013657 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-q8-quality-12.png) | 41.53 | 0.991667 | 0.007351 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-q8-13.png) | 32.35 | 0.976204 | 0.023774 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-bf16-fused-11.png) | 40.23 | 0.986699 | 0.013380 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/church-hybrid-q8-12-archived.png) | 30.22 | 0.969103 | 0.032721 |

## Prompt

Full-color indoor large-format photograph in a vertical 4-by-5 composition, showing the interior of a brutalist concrete church from a low, wide-angle viewpoint. Massive raw concrete walls rise around a cavernous nave, their surfaces marked by formwork seams, pinholes, chipped corners, and broad geometric planes. In the upper center, a narrow rectangular opening cuts through the thick wall as one slot of hard daylight falls diagonally into the otherwise dark sanctuary. The bright beam forms a single pale shaft across the center, revealing suspended dust particles against deep grey-brown shadow. One empty wooden pew stands alone within the light, placed off-center in the lower middle of the frame and facing the unseen altar beyond it. Its long plank seat has a dull brown finish, worn edges, visible grain, and two heavy supports; the backrest is bare, with no person or object resting on it. Behind the pew, the concrete architecture expands into angular buttresses and an overhanging ceiling slab that disappears into darkness. On the left, a recessed wall remains nearly black, while the right side contains a massive cantilevered concrete volume with a rough aggregate texture. At the far end, the daylight slot ends at a small altar-like projection of unadorned concrete, but its details remain lost in shadow. The floor consists of broad poured-concrete slabs with hairline joints and scattered grit. The concentrated beam illuminates only the pew and a thin patch of floor beneath it, leaving the surrounding nave in dense shadow.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
