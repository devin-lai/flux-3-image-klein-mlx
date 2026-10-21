"""Explicit, optional downloads from the five standalone Hugging Face releases."""
from pathlib import Path

NAMESPACE = 'devin-lai'
MODEL_NAME = 'flux-3-image-klein-mlx'
VARIANTS = ('q8-quality', 'q8', 'mixed', 'q4', 'bf16')


def download_variant(variant, destination, *, revision=None):
    if variant not in VARIANTS:
        raise ValueError(f'Unknown model variant: {variant}')
    root = Path(destination).expanduser().resolve()
    package = Path(__file__).resolve().parents[1]
    if root.is_relative_to(package):
        raise ValueError('Download models outside the installed runtime directory')
    # Do not combine two variant snapshots: stale weights would waste disk space.
    index_path = root / 'model_index.json'
    if index_path.exists():
        import json
        index = json.loads(index_path.read_text())
        if set(index.get('variants', {})) != {variant}:
            raise ValueError('Choose a separate model directory for each downloaded variant')
    try:
        from huggingface_hub import snapshot_download
    except ImportError as error:
        raise RuntimeError('Install optional Hub support: python -m pip install "huggingface_hub>=1,<3"') from error
    return Path(snapshot_download(
        repo_id=f'{NAMESPACE}/{MODEL_NAME}-{variant}',
        local_dir=root,
        revision=revision,
        library_name='mlx',
        library_version='0.1.0',
    ))
