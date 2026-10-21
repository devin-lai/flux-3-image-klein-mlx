# figurine — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 896 × 1120; seed **33**; category edit; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-figurine.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-bf16-anchor-16.png) | 29.41 | 0.968750 | 0.014951 |
| BF16 / 11 steps / fast | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-bf16-11.png) | 29.40 | 0.971826 | 0.017728 |
| Q8 + BF16 text / 11 steps | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-q8-quality-11.png) | 29.20 | 0.970045 | 0.018428 |
| Q8 + BF16 text / 12 steps | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-q8-quality-12.png) | 30.27 | 0.979651 | 0.013875 |
| Q8 + Q8 text / 13 steps | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-q8-13.png) | 31.06 | 0.973045 | 0.012486 |
| BF16 / 11 steps / fused | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-bf16-fused-11.png) | 29.48 | 0.972257 | 0.017546 |
| Hybrid Q8 / 12 steps / archived | [Original 896 × 1120 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/figurine-hybrid-q8-12-archived.png) | 29.03 | 0.961362 | 0.022286 |

## Prompt

Create a photograph of a painted tabletop figurine based on the mecha from the first image, displayed on a desk. Preserve the mecha’s exact design as the sculpted figure: the towering bipedal robot with its broad armored torso, mustard-yellow and muted sage-green color blocking, dark mechanical joints, heavy fists, three long cylindrical launchers rising from its back, compact head housing, and wide tracked feet. Translate it into a solid collectible figurine mounted on a small round black display base, with the original desert terrain simplified into a miniature sculpted base featuring pale sand, tiny rocks, sparse tufts of grass, and a few raised dust marks. Place the figurine upright at the center of a plain wooden desk under even daylight from a nearby window. Replace the original sky and desert background with an ordinary home-office setting: a closed gray notebook and black pen at frame-left, a ceramic mug at frame-right, and a small desk lamp behind the display. Show the figurine at a believable tabletop scale, with visible painted edges, subtle seam lines, and a clear support connection between its base and the sculpted terrain. Add a few loose model-making tools near the back edge of the desk, including a paintbrush and a small bottle of paint.

[Reference input 1](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/inputs/figurine-0.png)

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
