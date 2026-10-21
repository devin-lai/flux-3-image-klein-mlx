"""Ensure distribution wheels contain runtime source and no model payload."""
from pathlib import Path
from zipfile import ZipFile

wheels = list(Path('dist').glob('*.whl'))
assert wheels, 'Build a wheel first'
for wheel in wheels:
    with ZipFile(wheel) as archive:
        names = archive.namelist()
        assert 'flux_klein_mlx/__main__.py' in names
        assert 'flux_klein_mlx/engine.py' in names
        assert not any(n.endswith(('.safetensors', '.png', '.jpg')) for n in names)
        assert wheel.stat().st_size < 1024**2, 'Unexpectedly large runtime wheel'
    print(f'PASS: code-only wheel {wheel.name} ({wheel.stat().st_size:,} bytes)')
