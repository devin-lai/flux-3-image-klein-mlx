# field_notes — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1248 × 832; seed **2**; category typography; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-field_notes.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-bf16-anchor-16.png) | 37.93 | 0.993519 | 0.003544 |
| BF16 / 11 steps / fast | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-bf16-11.png) | 36.49 | 0.987975 | 0.009452 |
| Q8 + BF16 text / 11 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-q8-quality-11.png) | 33.97 | 0.983517 | 0.011323 |
| Q8 + BF16 text / 12 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-q8-quality-12.png) | 36.54 | 0.989928 | 0.006526 |
| Q8 + Q8 text / 13 steps | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-q8-13.png) | 34.47 | 0.988426 | 0.006638 |
| BF16 / 11 steps / fused | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-bf16-fused-11.png) | 36.30 | 0.987764 | 0.009588 |
| Hybrid Q8 / 12 steps / archived | [Original 1248 × 832 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/field_notes-hybrid-q8-12-archived.png) | 37.83 | 0.991276 | 0.005923 |

## Prompt

Close-up photograph of an open field notebook resting on a worn wooden table, viewed from a high three-quarter angle under diffused daylight. The cream paper pages fill most of the frame, with the notebook’s stitched binding running vertically through the center and one page corner curling upward. At the top of the right-hand page, handwritten in graphite pencil, the heading reads "Lake Vyrnwy, 14 October". Beneath it, four short lines of neat but uneven cursive handwriting read "wind NW, light", "two herons on the far shore", "water 9 degrees", and "the fog lifted at ten". Below the notes sits a small pencil sketch of a single standing heron in profile, drawn with a long neck, pointed beak, narrow body, and thin legs. A flattened pressed leaf rests beside the sketch near the lower left of the writing area, its muted green-brown surface held flat by the paper fibers. These are the only marks on the page. The left-hand page is blank apart from the paper grain and shallow creases. The tabletop consists of broad brown planks with dark seams, scratches, and visible wood grain, while the notebook casts a short shadow along its lower edge.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
