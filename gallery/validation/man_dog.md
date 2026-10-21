# man_dog — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1024 × 1024; seed **7**; category photo; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-man_dog.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-bf16-anchor-16.png) | 29.96 | 0.966976 | 0.024533 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-bf16-11.png) | 34.83 | 0.983950 | 0.012616 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-q8-quality-11.png) | 34.01 | 0.981368 | 0.014068 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-q8-quality-12.png) | 36.04 | 0.987478 | 0.008983 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-q8-13.png) | 37.30 | 0.990844 | 0.006380 |
| BF16 / 11 steps / fused | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-bf16-fused-11.png) | 34.74 | 0.983728 | 0.012829 |
| Hybrid Q8 / 12 steps / archived | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/man_dog-hybrid-q8-12-archived.png) | 36.04 | 0.987978 | 0.008919 |

## Prompt

Full-color outdoor photograph taken at eye level in the afternoon, with low sunlight coming from frame-right and casting long shadows across a neighborhood park. In the center, a white man in his thirties with fair skin, short brown hair, and light stubble walks along a paved path while holding a medium-sized golden retriever on a dark green leash. He wears a faded blue overshirt over a grey T-shirt, tan trousers, and worn brown walking shoes. His body faces left as he takes a step forward, looking down toward the dog with a neutral expression. The leash hangs in a loose curve between his right hand and the dog’s red collar. The golden retriever walks beside him on the left, its cream-gold coat lit along the back and ears, head lowered toward the grass and tail raised behind it. Dry leaves and small twigs lie near the edge of the path in the foreground. On the right, the sun sits just above the line of trees, producing a bright patch of glare and warm highlights on the man’s sleeve and the dog’s fur. Behind them, an open lawn extends toward scattered shrubs and mature tree trunks, with a wooden bench resting near the path. In the background, muted brick houses and parked cars form simple shapes beyond the foliage, while the pale blue sky occupies a narrow band above the treetops.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
