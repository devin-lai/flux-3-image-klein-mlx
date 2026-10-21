# Run FLUX.3 Image Klein on Apple Silicon

Use Python 3.12 on an Apple Silicon Mac. The validated setup uses MLX 0.32.4 on M5 with 32 GiB unified memory. Intel Macs, Windows and Linux do not run Metal inference.

## Install from GitHub

```sh
git clone https://github.com/devin-lai/flux-3-image-klein-mlx.git
cd flux-3-image-klein-mlx
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[hub]'
```

The Python package contains inference code, not model weights. All inference dependencies are pinned to the measured versions. Torch is used only in a separate CPU worker for seeded noise and schedule parity; MLX performs model inference.

## Download one pretrained model

```sh
flux-klein --download q8-quality --download-only --model-dir ../flux-models/q8-quality
flux-klein --model-dir ../flux-models/q8-quality --list
```

Choose `q8-quality`, `q8`, `mixed`, `q4` or `bf16`. Each public Hugging Face repository is complete and requires no authentication. Use a different directory for each variant. Downloads are 7.40–17.40 GiB depending on the model; Q8 quality is 12.73 GiB. Models must be stored outside the runtime checkout.

For a pinned download, use the published commit in [models.json](models.json):

```sh
flux-klein --download q8-quality --download-only \
  --revision 9414ab19ce2571a8cbb112074c2db597501e2025 \
  --model-dir ../flux-models/q8-quality
```

Alternatively, use `hf download devin-lai/flux-3-image-klein-mlx-q8-quality --local-dir ../flux-models/q8-quality`. No conversion or training is necessary. The original BFL checkpoint uses a different layout; use these prepared MLX variants with this loader.

## Generate an image

```sh
flux-klein --model-dir ../flux-models/q8-quality --preset q8-quality-16 \
  --prompt-file examples/teapot.json --width 768 --height 512 \
  --seed 1937 --out ../flux-output/teapot.png
```

Use `q8-quality-11` for the fastest locally measured quality preset, or `q8-quality-12` for closer reference agreement. See [all nine presets](PRESETS.md). Both dimensions must be multiples of 16 between 64 and 4096; larger canvases can need considerably more memory than the measured cases.

`--prompt-file` accepts UTF-8 text or JSON with a `prompt` field. Write a full scene caption describing subjects, materials, framing and lighting. The CLI sends the caption unchanged; use an LLM to expand a short request first if needed. The repository examples contain complete captions.

Outputs include a PNG, request JSON and metrics JSON. Choose a fresh output name each time, outside the model and runtime directories. Generation does not overwrite existing outputs. The metrics file reports pipeline timing; end-to-end process launch timing is measured separately by the [benchmark runner](benchmarks/README.md).

## Edit a reference image

This example uses the published benchmark input and its matching edit caption:

```sh
flux-klein --model-dir ../flux-models/q8-quality --preset q8-quality-16 \
  --image images/inputs/teapot_edit_small-0.png \
  --prompt-file examples/editing.json --width 768 --height 512 \
  --seed 8521 --out ../flux-output/red-teapot.png
```

For your own image, supply a full caption of the desired scene with the change folded in. Repeat `--image` for up to ten references; the published local benchmark covers single-reference editing only. Reference images guide the output and do not guarantee that every unedited pixel is preserved.

## Offline operation and integrity

After downloading, omit `--download`. No network download is initiated during ordinary inference. Verify selected components with:

```sh
flux-klein --model-dir ../flux-models/q8-quality --preset q8-quality-16 --verify
```

First verification reads the selected files to calculate SHA-256 checksums. Unchanged file identities are cached under `~/Library/Caches/flux-3-image-klein-mlx`. Set `FLUX_MLX_CACHE_DIR` to place this cache elsewhere, outside the model directory. A complete Hugging Face model download also provides `SHA256SUMS` for whole-package verification.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `Permission denied (publickey)` when cloning | Use `git clone https://github.com/devin-lai/flux-3-image-klein-mlx.git`. Public cloning needs no SSH key. For SSH, follow [GitHub's key setup](https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey). |
| `python3.12: command not found` | Install Python 3.12 for Apple Silicon, then create the virtual environment again. Check `python3.12 --version`. |
| `Generation requires an Apple Silicon Mac with Metal` | Use native arm64 Python on an Apple Silicon Mac. Check `python -c 'import platform; print(platform.machine())'`; it should print `arm64`. |
| Model metadata cannot be read | Download a complete variant and pass its directory using `--model-dir`. The source checkout has no weights. |
| Download destination is rejected | Choose a directory outside this checkout, such as `../flux-models/q8-quality`. |
| Existing output is rejected | Choose a new PNG filename; an interrupted run may have left its request JSON. |
| First run is slower | Downloads, full integrity checks and kernel compilation add overhead. Published timing used already-populated integrity caches. |
| Out of memory | Close memory-heavy applications, choose Q4/mixed or a smaller canvas. Minimum supported Mac memory has not been established; compact models have fidelity tradeoffs. |

Report issues with your Mac chip, memory, macOS, Python/package versions, full command and error. [Open an issue](https://github.com/devin-lai/flux-3-image-klein-mlx/issues/new/choose).

The runtime does not bundle a prompt upsampler or content filter. Review outputs before sharing and follow the [model license](licenses/FLUX-KOMMUNITY.md).
