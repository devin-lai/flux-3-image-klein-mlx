# Image stacks

Choose a runnable preset in the [model selection guide](../MODEL_SELECTION.md), then use the [inference loader](../USAGE.md). The names there map to the models and step counts shown below.

Original images and final parameters are included here. Contact sheets are labeled, reduced-resolution navigation aids; use the original PNG links for fidelity inspection. No images were regenerated for presentation. All links stay inside this release.

## Current MacBook Pro 32 GiB

Ten configurations per case: FP32/BF16/Q8-quality/Q8/mixed/Q4 at 16 steps, plus finalized BF16-11, Q8-quality-11/12 and Q8-13. Same input and seed; reduced-step measurements are later rounds.

- [man_dog — photo, 1024 × 1024](./local/man_dog.md)
- [teapot_small — photo, 768 × 512](./local/teapot_small.md)
- [poster_small — typography, 640 × 640](./local/poster_small.md)
- [teapot_edit_small — edit, 768 × 512](./local/teapot_edit_small.md)

## Archived validation

All 22 cases, including selection and inspected validation splits. Official FP32-16 and BF16 anchors accompany the final 11/12/13-step options. Hybrid-12 and BF16-fused-11 are archived alternatives.

- [man_dog — photo, 1024 × 1024](./validation/man_dog.md)
- [church — architecture, 832 × 1248](./validation/church.md)
- [fashion — photo, 832 × 1248](./validation/fashion.md)
- [hiroshige — illustration, 832 × 1248](./validation/hiroshige.md)
- [tea_tin — typography, 1024 × 1024](./validation/tea_tin.md)
- [gig_poster — typography, 832 × 1248](./validation/gig_poster.md)
- [field_notes — typography, 1248 × 832](./validation/field_notes.md)
- [balloons — layout, 1024 × 1024](./validation/balloons.md)
- [double_exposure_s1 — illustration, 832 × 1248](./validation/double_exposure_s1.md)
- [bandana — edit, 1024 × 1024](./validation/bandana.md)
- [coffee — edit, 1024 × 1024](./validation/coffee.md)
- [figurine — edit, 896 × 1120](./validation/figurine.md)
- [still_life_wide — photo, 1248 × 832](./validation/still_life_wide.md)
- [riso_lido — illustration, 832 × 1248](./validation/riso_lido.md)
- [knitted — layout, 1184 × 896](./validation/knitted.md)
- [cereal_box — typography, 832 × 1248](./validation/cereal_box.md)
- [double_exposure_s2 — illustration, 832 × 1248](./validation/double_exposure_s2.md)
- [cactus — edit, 1024 × 1024](./validation/cactus.md)
- [mugprint — multi-edit, 1024 × 1024](./validation/mugprint.md)
- [teapot_small — photo, 768 × 512](./validation/teapot_small.md)
- [poster_small — typography, 640 × 640](./validation/poster_small.md)
- [teapot_edit_small — edit, 768 × 512](./validation/teapot_edit_small.md)

## Archived previews

Earlier 6/8-step results. Reference is FP32 at 8 steps; images are archived repeat means, with older runtime settings. Previous Q8/Q4 weights are not shipped.

- [man_dog — photo, 1024 × 1024](./previews/man_dog.md)
- [teapot_small — photo, 768 × 512](./previews/teapot_small.md)
- [poster_small — typography, 640 × 640](./previews/poster_small.md)
- [teapot_edit_small — edit, 768 × 512](./previews/teapot_edit_small.md)
