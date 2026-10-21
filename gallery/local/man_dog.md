# man_dog — Current MacBook Pro 32 GiB

Ten configurations per case: FP32/BF16/Q8-quality/Q8/mixed/Q4 at 16 steps, plus finalized BF16-11, Q8-quality-11/12 and Q8-13. Same input and seed; reduced-step measurements are later rounds.

Canvas 1024 × 1024; seed **7**; category photo; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/local-man_dog.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| MLX FP32 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/man_dog-fp32.png) | ∞ | 1.000000 | 0.000000 |
| BF16 / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/man_dog-bf16.png) | 53.39 | 0.999549 | 0.000143 |
| Q8 + BF16 text / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/man_dog-q8-quality.png) | 40.68 | 0.995973 | 0.002346 |
| Q8 + Q8 text / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/man_dog-q8.png) | 39.55 | 0.994783 | 0.003346 |
| Mixed 4/8 + Q8 text / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/man_dog-mixed.png) | 26.41 | 0.935084 | 0.050433 |
| Q4 + Q8 text / 16 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-16/man_dog-q4.png) | 27.48 | 0.936144 | 0.046756 |
| BF16 / 11 steps / fast | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/man_dog-bf16-11.png) | 34.78 | 0.983806 | 0.012697 |
| Q8 + BF16 text / 11 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/man_dog-q8-quality-11.png) | 34.02 | 0.981402 | 0.014055 |
| Q8 + BF16 text / 12 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/man_dog-q8-quality-12.png) | 36.06 | 0.987531 | 0.008994 |
| Q8 + Q8 text / 13 steps | [Original 1024 × 1024 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/local-presets/man_dog-q8-13.png) | 37.33 | 0.990936 | 0.006361 |

## Prompt

Full-color outdoor photograph taken at eye level in the afternoon, with low sunlight coming from frame-right and casting long shadows across a neighborhood park. In the center, a white man in his thirties with fair skin, short brown hair, and light stubble walks along a paved path while holding a medium-sized golden retriever on a dark green leash. He wears a faded blue overshirt over a grey T-shirt, tan trousers, and worn brown walking shoes. His body faces left as he takes a step forward, looking down toward the dog with a neutral expression. The leash hangs in a loose curve between his right hand and the dog’s red collar. The golden retriever walks beside him on the left, its cream-gold coat lit along the back and ears, head lowered toward the grass and tail raised behind it. Dry leaves and small twigs lie near the edge of the path in the foreground. On the right, the sun sits just above the line of trees, producing a bright patch of glare and warm highlights on the man’s sleeve and the dog’s fur. Behind them, an open lawn extends toward scattered shrubs and mature tree trunks, with a wooden bench resting near the path. In the background, muted brick houses and parked cars form simple shapes beyond the foliage, while the pale blue sky occupies a narrow band above the treetops.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
