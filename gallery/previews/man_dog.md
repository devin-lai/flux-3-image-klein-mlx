# man_dog — Archived previews

Earlier 6/8-step results. Reference is FP32 at 8 steps; images are archived repeat means, with older runtime settings. Previous Q8/Q4 weights are not shipped.

Canvas 1024 × 1024; seed **7**; category photo; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/previews-man_dog.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official FP32 / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-official-fp32-8.png) | ∞ | 1.000000 | not measured |
| Previous 8-bit / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-previous-q8-8.png) | 31.03 | 0.960284 | not measured |
| Previous 4-bit / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-previous-q4-8.png) | 19.14 | 0.669131 | not measured |
| 8-bit / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-q8-8.png) | 37.00 | 0.988010 | not measured |
| 4-bit / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-q4-8.png) | 25.59 | 0.860017 | not measured |
| Mixed 4/8-bit / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-mixed-8.png) | 25.26 | 0.871322 | not measured |
| BF16 control / 8 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-bf16-8.png) | 42.77 | 0.996176 | not measured |
| Mixed 4/8-bit / 6 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/previews/man_dog-mixed-6.png) | 22.48 | 0.769897 | not measured |

## Prompt

Full-color outdoor photograph taken at eye level in the afternoon, with low sunlight coming from frame-right and casting long shadows across a neighborhood park. In the center, a white man in his thirties with fair skin, short brown hair, and light stubble walks along a paved path while holding a medium-sized golden retriever on a dark green leash. He wears a faded blue overshirt over a grey T-shirt, tan trousers, and worn brown walking shoes. His body faces left as he takes a step forward, looking down toward the dog with a neutral expression. The leash hangs in a loose curve between his right hand and the dog’s red collar. The golden retriever walks beside him on the left, its cream-gold coat lit along the back and ears, head lowered toward the grass and tail raised behind it. Dry leaves and small twigs lie near the edge of the path in the foreground. On the right, the sun sits just above the line of trees, producing a bright patch of glare and warm highlights on the man’s sleeve and the dog’s fur. Behind them, an open lawn extends toward scattered shrubs and mature tree trunks, with a wooden bench resting near the path. In the background, muted brick houses and parked cars form simple shapes beyond the foliage, while the pale blue sky occupies a narrow band above the treetops.

Scores in this page are relative to the archived FP32-8 repeat mean. The images were produced with the recorded earlier inputs; the case prompt above is shared with the current suite.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
