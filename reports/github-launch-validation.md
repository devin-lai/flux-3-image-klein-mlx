# GitHub launch validation

The source release retains the published numerical runtime. The GitHub launch adds packaging metadata, documentation, benchmark tools, community templates and presentation assets.

- Seven existing software tests passed on Python 3.12.14.
- The published-data audit passed for all 120 raw measurement records, including geometric means, memory peaks, speed ratios and repeated image hashes.
- A fresh-process Q8-quality-16 generation of the 768 × 512 teapot (seed 1937) reproduced the published PNG bytes exactly. This was a smoke check, not a replacement benchmark round.
- The runtime wheel contains code and license metadata only; no model weights or gallery images.
- Public Hugging Face variant repositories were checked for unauthenticated access.

The original [runtime validation](runtime-validation.md) and [120-run benchmark](macbook-pro-32gb.md) provide the earlier inference and performance evidence.
