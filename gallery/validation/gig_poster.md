# gig_poster — Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

Canvas 832 × 1248; seed **1**; category typography; archived split selection.

![Labeled comparison stack](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/stacks/validation-gig_poster.jpg)

## Original PNGs

| Configuration | Image | PSNR dB | SSIM | LPIPS |
|---|---|---:|---:|---:|
| Official-code FP32 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-official-fp32-16.png) | reference | reference | reference |
| Published official BF16 / 16 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-bf16-anchor-16.png) | 26.27 | 0.969342 | 0.015225 |
| BF16 / 11 steps / fast | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-bf16-11.png) | 31.38 | 0.986074 | 0.009168 |
| Q8 + BF16 text / 11 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-q8-quality-11.png) | 29.62 | 0.980651 | 0.012831 |
| Q8 + BF16 text / 12 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-q8-quality-12.png) | 29.66 | 0.982442 | 0.011374 |
| Q8 + Q8 text / 13 steps | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-q8-13.png) | 32.13 | 0.988046 | 0.008071 |
| BF16 / 11 steps / fused | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-bf16-fused-11.png) | 31.29 | 0.985841 | 0.009425 |
| Hybrid Q8 / 12 steps / archived | [Original 832 × 1248 PNG](https://huggingface.co/devin-lai/flux-3-image-klein-mlx/resolve/fc8c4a48e9de69e75528739ec6752e219aac0de2/images/validation/gig_poster-hybrid-q8-12-archived.png) | 28.01 | 0.976925 | 0.013431 |

## Prompt

Studio photograph of a letterpress gig poster printed on thick cream paper stock, shown straight-on against a plain neutral background with even, shadowless lighting. The rectangular sheet fills most of the frame, its deckled fibers and fine paper grain visible around the edges. A strict two-ink composition uses only black and brick red ink, with no illustrations, borders, logos, or additional wording. At the top, very large black wood type reads "THE LOW TIDES", set in bold uppercase slab-serif letters with uneven hand-pressed edges and shallow brick-red registration marks confined to the ink impressions. Directly below, small brick-red serif text reads "with special guests". In the center, medium-sized black wood type reads "MOTH LIGHT", followed by medium brick-red wood type reading "HARBOUR SOUND", both centered on separate lines with generous spacing. Along the bottom, compact black small-cap lettering reads "Saturday 21 March, Doors 8pm, The Old Chapel, Margate". Beneath it, smaller brick-red small caps read "Tickets 12 pounds". The typography is centered vertically and horizontally, with minor ink spread and irregular pressure texture characteristic of traditional letterpress printing; every other area remains unprinted cream stock.

[All stacks](../README.md) · [Final presets](../../PRESETS.md) · [Test report](../../reports/macbook-pro-32gb.md)
