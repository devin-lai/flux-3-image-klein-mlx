"""Read-only model files with mutable checksum identities outside the package."""
import hashlib
import os
from pathlib import Path

EXPORT_ROOT = Path(os.environ.get('FLUX_MLX_MODEL_ROOT', Path(__file__).resolve().parents[1])).expanduser().resolve()
CACHE = Path(os.environ.get('FLUX_MLX_CACHE_DIR', Path.home()/'Library/Caches/flux-3-image-klein-mlx')).expanduser().resolve()
if CACHE.is_relative_to(EXPORT_ROOT):
    raise ValueError('The runtime cache must be outside the model directory')


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as source:
        for block in iter(lambda: source.read(8*1024**2), b''):
            digest.update(block)
    return digest.hexdigest()


def verification_cache(model_dir):
    key = hashlib.sha256(str(Path(model_dir).resolve()).encode()).hexdigest()
    return CACHE/'verification'/f'{key}.json'
