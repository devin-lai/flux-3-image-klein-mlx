"""Generate an image with the finalized MLX model artifacts."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import platform


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-dir', type=Path, default=Path(__file__).resolve().parents[1], help='Directory containing model_index.json and model components')
    parser.add_argument('--list', action='store_true', help='List runnable presets without loading MLX or weights')
    parser.add_argument('--preset', help='Preset from --list; default: the downloaded model\'s 16-step preset')
    from .hub import VARIANTS
    parser.add_argument('--download', choices=VARIANTS, help='Download just this variant from Hugging Face before running')
    parser.add_argument('--download-only', action='store_true', help='Download the selected variant and exit')
    parser.add_argument('--revision', help='Pin a Hub commit or tag when using --download')
    prompt = parser.add_mutually_exclusive_group()
    prompt.add_argument('--prompt')
    prompt.add_argument('--prompt-file', type=Path, help='UTF-8 prompt or JSON with a prompt field')
    parser.add_argument('--width', type=int, default=1024)
    parser.add_argument('--height', type=int, default=1024)
    parser.add_argument('--seed', type=int, default=7)
    parser.add_argument('--image', type=Path, action='append', default=[], help='Reference image; repeat for multiple references')
    parser.add_argument('--out', type=Path, help='PNG destination outside the model directory')
    parser.add_argument('--verify', action='store_true', help='Verify selected component checksums and exit')
    args = parser.parse_args()
    root = args.model_dir.expanduser().resolve()
    if (args.download_only or args.revision) and not args.download:
        parser.error('--download-only and --revision require --download')
    if args.download:
        from .hub import download_variant
        try:
            download_variant(args.download, root, revision=args.revision)
        except (ValueError, RuntimeError) as error:
            parser.error(str(error))
        if args.download_only:
            print(f'Downloaded {args.download} to {root}')
            return
    try:
        index = json.loads((root/'model_index.json').read_text())
        definitions = json.loads((root/'presets.json').read_text())['presets']
    except (OSError, ValueError) as error:
        parser.error(f'Cannot read model metadata at {root}: {error}')
    # Archived experiments remain in the reports, but are not selectable recipes.
    names = ['bf16-16', 'q8-quality-16', 'q8-16', 'mixed-16', 'q4-16',
             'bf16-11', 'q8-quality-11', 'q8-quality-12', 'q8-13']
    available = {name: definitions[name] for name in names
                 if name in definitions and definitions[name]['variant'] in index['variants']}
    args.preset = args.preset or f"{index.get('default_variant', 'q8-quality')}-16"
    if args.list:
        for name, spec in available.items():
            variant = index['variants'][spec['variant']]
            print(f"{name:18} {spec['steps']:2} steps  transformer={variant['transformer']:5} text={variant['text_encoder']:4}  {variant['download_bytes']/2**30:.2f} GiB download")
        return
    if args.preset not in available:
        parser.error('Unknown or archived preset; use --list')
    if platform.system() != 'Darwin' or platform.machine() != 'arm64':
        parser.error('Generation requires an Apple Silicon Mac with Metal')
    spec = available[args.preset]
    variant = index['variants'][spec['variant']]
    if any(n < 64 or n > 4096 or n % 16 for n in (args.width, args.height)):
        parser.error('Width and height must be multiples of 16 between 64 and 4096')
    if len(args.image) > 10:
        parser.error('At most 10 reference images are supported')
    if not 0 <= args.seed < 2**63:
        parser.error('Seed must be between 0 and 2**63 - 1')
    references = [str(p.expanduser().resolve()) for p in args.image]
    for p in references:
        if not Path(p).is_file():
            parser.error(f'Reference image does not exist: {p}')
    output = args.out.expanduser().resolve() if args.out else None
    if not args.verify:
        if output is None or output.suffix.lower() != '.png':
            parser.error('--out must be a PNG path')
        package = Path(__file__).resolve().parents[1]
        if output.is_relative_to(root) or output.is_relative_to(package):
            parser.error('Output must be outside the model and installed runtime directories')
        for p in (output, output.with_suffix('.json'), output.with_suffix('.metrics.json')):
            if p.exists():
                parser.error(f'Output already exists: {p}')
        if not (args.prompt or args.prompt_file):
            parser.error('Supply --prompt or --prompt-file')
        caption = args.prompt
        if args.prompt_file:
            try:
                caption = args.prompt_file.read_text()
                if args.prompt_file.suffix.lower() == '.json':
                    caption = json.loads(caption)['prompt']
            except (OSError, ValueError, KeyError) as error:
                parser.error(f'Cannot read prompt: {error}')
        if not isinstance(caption, str) or not caption.strip():
            parser.error('Prompt must not be empty')
    # Fix arithmetic before importing MLX; never inherit a different TF32 default.
    os.environ['MLX_ENABLE_TF32'] = '0'
    os.environ['FLUX_MLX_MODEL_ROOT'] = str(root)
    from .pipeline import generate, verify_export
    components = {root/variant['transformer']: {'transformer'}}
    if references:
        components[root/variant['transformer']].add('image_conditioning')
    components.setdefault(root/variant['text_encoder'], set()).add('text_encoder')
    if args.verify:
        for directory, used in components.items():
            verify_export(directory, components=used)
        print(f'Checksums verified for {args.preset}')
        return
    request = dict(prompt=caption, width=args.width, height=args.height, seed=args.seed,
                   steps=spec['steps'], guidance=None, alpha=6.93, references=references,
                   profile=args.preset, transformer=variant['transformer'], text_encoder=variant['text_encoder'])
    if spec.get('grid_indices'):
        request['grid'] = spec['grid_indices']
    output.parent.mkdir(parents=True, exist_ok=True)
    from .common import write_json
    write_json(output.with_suffix('.json'), request)
    metrics = generate(request, output, vae_dtype=spec['vae_dtype'], cache_mb=spec['cache_MiB'],
                       kernel_mode=spec['kernel_mode'], dit_dtype='float32', precision='scaled')
    write_json(output.with_suffix('.metrics.json'), metrics)
    print(f"Saved {output}; {metrics['wall_seconds']:.2f}s model pipeline; peak physical {metrics['peak_physical_footprint_bytes']/2**30:.2f} GiB")


if __name__ == '__main__':
    main()
