"""Recompute published latency, memory, determinism and speedups from raw runs."""
from collections import defaultdict
import json
import math
from pathlib import Path
from statistics import geometric_mean, median

ROOT = Path(__file__).resolve().parents[1]


def audit(path, reference_seconds=None):
    data = json.loads(path.read_text())
    assert data['complete'] and len(data['measurements']) == data['runs'], path
    groups = defaultdict(list)
    for row in data['measurements']:
        assert row['launch_seconds'] > 0 and row['physical_peak_bytes'] > 0
        groups[row['variant'], row['case']].append(row)
    variants = defaultdict(list)
    for (variant, case), rows in groups.items():
        assert len(rows) == 3 and len({r['repeat'] for r in rows}) == 3, (variant, case)
        measured = median(r['launch_seconds'] for r in rows)
        assert math.isclose(measured, data['by_case'][case][variant]['median_seconds'], rel_tol=1e-9)
        assert len({r['image_sha256'] for r in rows}) == 1, (variant, case, 'non-deterministic')
        variants[variant].append((measured, max(r['physical_peak_bytes'] for r in rows) / 2**30))
    assert set(variants) == set(data['aggregate'])
    baseline = reference_seconds or data['aggregate']['fp32']['geomean_seconds']
    for variant, observations in variants.items():
        assert len(observations) == 4, variant
        seconds = geometric_mean(v[0] for v in observations)
        memory = max(v[1] for v in observations)
        expected = data['aggregate'][variant]
        assert math.isclose(seconds, expected['geomean_seconds'], rel_tol=1e-9), variant
        assert math.isclose(memory, expected['max_physical_GiB'], rel_tol=1e-9), variant
        ratio_key = 'speedup_vs_prior_fp32' if reference_seconds else 'speedup'
        assert math.isclose(baseline / seconds, expected[ratio_key], rel_tol=1e-9), variant
        print(f'{variant:18} {seconds:7.2f} s  {baseline / seconds:4.2f}x  {memory:5.2f} GiB')
    return baseline, data['runs']


if __name__ == '__main__':
    reference, first = audit(ROOT / 'results/m5-32gb-16step.json')
    _, second = audit(ROOT / 'results/m5-32gb-presets.json', reference)
    print(f'PASS: {first + second} runs; all aggregate latencies, memory, speedups and repeat hashes agree.')
