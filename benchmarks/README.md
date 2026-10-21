# Reproduce and audit the benchmark

The published evidence contains **120 fresh-process runs**: six 16-step configurations × four workloads × three repeats, plus four reduced-step configurations × four workloads × three repeats. All existing measurements remain unchanged.

## Audit the published arithmetic without a model

```sh
python scripts/audit_benchmarks.py
```

This standard-library script recomputes the four-workload geometric means from per-workload medians, maximum process physical memory, speed ratios, repeat counts and identical output hashes. It checks the archived raw records against their aggregates; it does not rerun inference or independently validate the original timing instrumentation.

## Run on your Mac

Install the runtime and download a complete model following [USAGE.md](../USAGE.md). Prepopulate the verification cache if you want conditions closer to the original timing suite:

```sh
flux-klein --model-dir ../flux-models/q8-quality --preset q8-quality-16 --verify
python benchmarks/run.py --model-dir ../flux-models/q8-quality \
  --presets q8-quality-16 q8-quality-11 --repeats 3 \
  --out ../benchmark-output/q8-quality
```

The runner creates a fresh process per request and rotates preset order. It records end-to-end launch time through PNG/metrics output, peak lifetime process physical footprint, MLX allocation, output hashes, per-case medians/ranges and aggregate latency. Output must be a new directory outside the checkout and model directory. It never downloads models. Three repeats, four cases and two presets take several minutes; a one-case smoke run is:

```sh
python benchmarks/run.py --model-dir ../flux-models/q8-quality \
  --presets q8-quality-16 --cases teapot_small --repeats 1 --cooldown 0 \
  --out ../benchmark-output/smoke
```

The strict FP32 control uses the complete BF16 variant. Run it separately with its own model directory:

```sh
python benchmarks/run.py --model-dir ../flux-models/bf16 \
  --presets fp32-16 bf16-16 --repeats 3 --out ../benchmark-output/bf16-control
```

The runner reproduces the public inference configurations and case inputs. Its process timing implementation is newly provided for community reproduction; it is not the original private collection script. It does not compute LPIPS/SSIM/PSNR or sample process-tree memory. Original published runs include those additional measurements. Record your model revision, runtime commit, AC/battery state, power mode, background load and whether verification caches were populated. Do not merge results from different machines or measurement rounds into one unlabeled speedup.

## Interpret the numbers

- Launch time includes process startup, imports, integrity verification, weight loading, text encoding, denoising, VAE decoding and output. Pipeline time in the metrics JSON is a different interval.
- Peak process physical footprint includes Metal memory. MLX allocation is a separate measure and must not be added to it.
- The strict control upcasts BF16 checkpoint values on demand and runs FP32 arithmetic, portable kernels and FP32 VAE execution. It is not a fully FP32-resident checkpoint.
- Reduced steps change the trajectory; the 5.43× published ratio uses a later timing round against the earlier FP32 control.
- Four local workloads establish those cases, not every prompt, canvas or Mac. The separate 22-case validation is archived quality evidence.

[Published methodology](../reports/macbook-pro-32gb.md) · [16-step raw records](../results/m5-32gb-16step.json) · [Reduced-step records](../results/m5-32gb-presets.json)
