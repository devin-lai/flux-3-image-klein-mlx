"""Small CPU-only worker preserving the reference Torch RNG and time schedule."""
import argparse
import numpy as np
import torch


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--tokens", type=int, required=True)
    parser.add_argument("--steps", type=int, required=True)
    parser.add_argument("--grid", help="Comma-separated indices into the official 16-step timesteps")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    noise = torch.randn((args.tokens, 128), generator=torch.Generator().manual_seed(args.seed))
    noise = noise.to(torch.bfloat16).float().numpy()
    t = torch.linspace(1., 0., (16 if args.grid else args.steps) + 1)
    schedule = (6.93 * t / (1. + (6.93 - 1.) * t)).numpy()
    if args.grid:
        # A subset of the official 16-step timesteps: the trajectory visits only those times.
        schedule = schedule[[int(i) for i in args.grid.split(",")]]
        if len(schedule) != args.steps + 1:
            raise SystemExit("--grid must list steps + 1 timesteps")
    np.savez(args.output, noise=noise, schedule=schedule)


if __name__ == "__main__":
    main()
