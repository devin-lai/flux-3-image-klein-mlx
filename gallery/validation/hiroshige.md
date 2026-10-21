# hiroshige — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category illustration; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-hiroshige.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-bf16-anchor-16.png) | 28.00 | 0.968729 | 0.016026 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-bf16-11.png) | 28.44 | 0.957348 | 0.022392 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-q8-quality-11.png) | 27.84 | 0.951536 | 0.024358 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-q8-quality-12.png) | 30.81 | 0.973895 | 0.013736 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-q8-13.png) | 25.57 | 0.948121 | 0.025194 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-bf16-fused-11.png) | 28.45 | 0.957361 | 0.022397 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/hiroshige-hybrid-q8-12-archived.png) | 27.63 | 0.960265 | 0.018145 |

## Prompt

Traditional Japanese woodblock print in the Hiroshige register, rendered entirely in indigo and sumi ink on warm off-white washi paper with visible fibers and uneven carved edges. A broad wooden bridge crosses a rushing river from the lower left toward the center-right, its dark timber planks and low railings reduced to crisp, rhythmic lines. Sudden rain fills the upper half of the composition as dense, fine parallel indigo lines slanting diagonally across the entire scene. Above the bridge, layered blue-grey storm clouds sweep over distant mountains, their flattened silhouettes breaking into pale mist and deep indigo cloud bands. In the foreground, three small travelers stand close together beneath umbrellas on the bridge: one figure in a dark robe holds a round indigo umbrella, another carries a black umbrella, and a third wears a muted grey cloak beneath a smaller umbrella. Their bodies lean forward against the downpour, with hems and sleeves bending in the wind. Below them, white water surges around the bridge supports in curling sumi waves marked by sparse indigo foam crests. On the left bank, reeds and wet grasses rise beside a cluster of dark rocks; on the right, a windswept pine bends over the riverbank. The restrained composition uses broad areas of untouched paper, flat color separations, irregular hand-printed registration, and no lettering, seals, captions, or decorative inscriptions anywhere.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
