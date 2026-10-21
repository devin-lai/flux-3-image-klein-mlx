# knitted — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 1184 × 896; seed **1**; category layout; archived split holdout.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-knitted.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-bf16-anchor-16.png) | 31.83 | 0.971626 | 0.012147 |
| BF16 / 11 steps / fast | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-bf16-11.png) | 30.94 | 0.953979 | 0.021848 |
| Q8 + BF16 text / 11 steps | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-q8-quality-11.png) | 30.69 | 0.953983 | 0.022221 |
| Q8 + BF16 text / 12 steps | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-q8-quality-12.png) | 33.94 | 0.977819 | 0.011447 |
| Q8 + Q8 text / 13 steps | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-q8-13.png) | 34.38 | 0.978794 | 0.010442 |
| BF16 / 11 steps / fused | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-bf16-fused-11.png) | 30.91 | 0.953852 | 0.021913 |
| Hybrid Q8 / 12 steps / archived | [Original 1184 × 896 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/knitted-hybrid-q8-12-archived.png) | 33.97 | 0.976283 | 0.011843 |

## Prompt

Macro photograph of a chunky knitted soft sculpture diorama, lit by a low, directional light source from the left that casts long, deep shadows across the textures. Filling the upper background is a dark indigo knitted backdrop. Across the lower third, a chaotic bed of thick looped yarn forms a churning sea. Rising from this base are three massive, conical icebergs constructed of stark white cable-knit yarn, positioned in a rhythmic frontal row: one on the left <iceberg_1>, a slightly taller one on the right <iceberg_2>, and a bulky central peak <iceberg_3>. Clinging to the slopes of the outer icebergs is a rhythmic repetition of tiny, identical pale blue knitted houses. Suspended in the upper frame between the peaks is a slightly curling strip of cream-colored stockinette fabric, bearing thick embroidered text <En_Text_1>. Disrupting the icy white and blue palette, a giant, vibrant magenta knitted whale tail <whale_tail_1> bursts vertically from the center of the teal sea, its thick ribbed surface covered in a halo of stray wool fibers illuminated by the raking light. [{"id": "iceberg_1", "bbox": [300, 50, 750, 350], "desc": "A conical soft sculpture made of stark white, chunky roving yarn in a thick cable-knit pattern. The left side is brightly lit, while the right side falls into deep, fuzzy shadow."}, {"id": "iceberg_2", "bbox": [250, 650, 750, 950], "desc": "A tall, asymmetrical peak of white cable-knit yarn, featuring a few visibly dropped stitches near the base and slightly uneven tension in the cables."}, {"id": "iceberg_3", "bbox": [200, 300, 650, 700], "desc": "The largest central iceberg, a bulky mound of white and pale grey ribbed knitting, dominating the midground with thick, vertical columns of stitches."}, {"id": "En_Text_1", "bbox": [130, 220, 220, 780], "desc": "The exact words \"KNITTED ICEBERG VILLAGE\" embroidered in thick, raised navy-blue yarn across the cream banner. The lettering is slightly uneven and puckered, conforming to the physical stretch of the knitted fabric beneath it."}, {"id": "whale_tail_1", "bbox": [500, 380, 850, 620], "desc": "A giant whale tail knitted from bright magenta and coral-pink yarn, bursting vertically from the teal sea. It features thick ribs, a slightly asymmetrical fluke, and a fuzzy halo of stray wool fibers caught in the directional light."}]

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
