"""Fresh-process benchmark runner. No model download is performed by this script."""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import platform
from statistics import geometric_mean, median
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
LOCAL_CASES = ('man_dog', 'teapot_small', 'poster_small', 'teapot_edit_small')


def worker(model_root, preset, case, output):
    os.environ['MLX_ENABLE_TF32'] = '0'
    os.environ['FLUX_MLX_MODEL_ROOT'] = str(model_root)
    sys.path.insert(0, str(ROOT))
    from flux_klein_mlx.pipeline import generate
    definitions = json.loads((model_root / 'presets.json').read_text())['presets']
    index = json.loads((model_root / 'model_index.json').read_text())
    if preset == 'fp32-16':
        spec = dict(variant='bf16', steps=16, kernel_mode='portable', vae_dtype='float32', cache_MiB=512)
    else:
        spec = definitions[preset]
    variant = index['variants'][spec['variant']]
    references = []
    for reference in case.get('references', []):
        path = ROOT / reference['image']
        if hashlib.sha256(path.read_bytes()).hexdigest() != reference['sha256']:
            raise ValueError(f'Reference checksum mismatch: {path.name}')
        references.append(str(path))
    request = dict(prompt=case['prompt'], width=case['width'], height=case['height'], seed=case['seed'],
                   steps=spec['steps'], guidance=None, alpha=6.93, references=references, profile=preset,
                   transformer=variant['transformer'], text_encoder=variant['text_encoder'])
    if spec.get('grid_indices'):
        request['grid'] = spec['grid_indices']
    output.with_suffix('.request.json').write_text(json.dumps(request, indent=2))
    metrics = generate(request, output, vae_dtype=spec['vae_dtype'], cache_mb=spec['cache_MiB'],
                       kernel_mode=spec['kernel_mode'], dit_dtype='float32',
                       precision='fp32' if preset == 'fp32-16' else 'scaled')
    output.with_suffix('.metrics.json').write_text(json.dumps(metrics, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-dir', required=True, type=Path)
    parser.add_argument('--presets', nargs='+', default=['q8-quality-16', 'q8-quality-11'])
    parser.add_argument('--cases', nargs='+', choices=LOCAL_CASES, default=list(LOCAL_CASES))
    parser.add_argument('--repeats', type=int, default=3)
    parser.add_argument('--cooldown', type=float, default=5.)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--worker', nargs=3, help=argparse.SUPPRESS)
    args = parser.parse_args()
    model_root, output_root = args.model_dir.expanduser().resolve(), args.out.expanduser().resolve()
    if args.worker:
        preset, case_id, output = args.worker
        case = next(c for c in json.loads((ROOT / 'results/cases.json').read_text()) if c['id'] == case_id)
        worker(model_root, preset, case, Path(output))
        return
    if platform.system() != 'Darwin' or platform.machine() != 'arm64':
        parser.error('Benchmarks require an Apple Silicon Mac')
    if args.repeats < 1 or args.cooldown < 0:
        parser.error('Use at least one repeat and a nonnegative cooldown')
    if output_root.exists() or output_root.is_relative_to(ROOT) or output_root.is_relative_to(model_root):
        parser.error('--out must be a new directory outside the source and model directories')
    index = json.loads((model_root / 'model_index.json').read_text())
    definitions = json.loads((model_root / 'presets.json').read_text())['presets']
    for preset in args.presets:
        variant = 'bf16' if preset == 'fp32-16' else definitions.get(preset, {}).get('variant')
        if variant not in index['variants']:
            parser.error(f'{preset} is not available in this model directory')
    if len(set(args.presets)) != len(args.presets) or len(set(args.cases)) != len(args.cases):
        parser.error('Presets and cases must be unique')
    output_root.mkdir(parents=True)
    report = dict(format_version=1, machine=dict(system=platform.system(), release=platform.release(),
                  architecture=platform.machine(), python=platform.python_version(),
                  chip=subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string'], text=True).strip(),
                  memory_bytes=int(subprocess.check_output(['sysctl', '-n', 'hw.memsize'], text=True))),
                  timing='fresh-process launch through PNG and metrics output; ordinary filesystem/driver caches',
                  cache_conditions='caller must record whether component verification caches were prepopulated',
                  measurements=[], complete=False)
    for repeat in range(args.repeats):
        for case_index, case in enumerate(args.cases):
            offset = (repeat + case_index) % len(args.presets)
            for preset in args.presets[offset:] + args.presets[:offset]:
                stem = f'{case}-{preset}-r{repeat}'
                output = output_root / (stem + '.png')
                command = [sys.executable, str(Path(__file__).resolve()), '--model-dir', str(model_root),
                           '--out', str(output_root), '--worker', preset, case, str(output)]
                print(f'Running {stem}', flush=True)
                start = time.perf_counter()
                with (output_root / (stem + '.log')).open('w') as log:
                    subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, check=True)
                elapsed = time.perf_counter() - start
                metrics = json.loads(output.with_suffix('.metrics.json').read_text())
                report['measurements'].append(dict(case=case, preset=preset, repeat=repeat,
                    launch_seconds=elapsed, physical_peak_bytes=metrics['peak_physical_footprint_bytes'],
                    mlx_peak_bytes=metrics['peak_mlx_active_bytes'], image_sha256=hashlib.sha256(output.read_bytes()).hexdigest()))
                (output_root / 'benchmark.json').write_text(json.dumps(report, indent=2))
                time.sleep(args.cooldown)
    groups = defaultdict(list)
    for row in report['measurements']:
        groups[row['preset'], row['case']].append(row)
    report['by_case'] = {f'{p}/{c}': dict(median_seconds=median(r['launch_seconds'] for r in rows),
        min_seconds=min(r['launch_seconds'] for r in rows), max_seconds=max(r['launch_seconds'] for r in rows),
        deterministic=len({r['image_sha256'] for r in rows}) == 1) for (p,c),rows in groups.items()}
    report['aggregate'] = {p: dict(geomean_seconds=geometric_mean(median(r['launch_seconds'] for r in groups[p,c]) for c in args.cases),
        max_physical_GiB=max(r['physical_peak_bytes'] for r in report['measurements'] if r['preset']==p)/2**30)
        for p in args.presets}
    report['complete'] = True
    (output_root / 'benchmark.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report['aggregate'], indent=2))


if __name__ == '__main__':
    main()
