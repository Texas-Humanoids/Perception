# training/isaaclab

Policy training with [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) 3.0
on Isaac Sim 6.1. See [`../README.md`](../README.md) for how this fits with
the other simulator.

We're on **3.0.0rc1**, NVIDIA's Early Access release: features are frozen and
only bug fixes are going in. General availability is targeted for the end of
October 2026; bump the pin when it ships.

## Requirements

From the [Isaac Sim 6.1 requirements](https://docs.isaacsim.omniverse.nvidia.com/6.1.0/installation/requirements.html):

- Ubuntu 22.04 or 24.04, x86_64. **There is no macOS support.**
- At least a GeForce RTX 4080 (16 GB VRAM) and 32 GB RAM
- NVIDIA driver 595.58.03 (the version Isaac Sim 6.1 was tested on)

## Setup

```bash
cd training/isaaclab
uv sync
```

This is a large download. Then train a cartpole for a few iterations with
each physics backend:

```bash
# MuJoCo Warp physics (the same engine mjlab uses). Doesn't start Isaac Sim.
uv run isaaclab train --rl_library rsl_rl --task Isaac-Cartpole \
    --num_envs 64 --max_iterations 5 physics=newton_mjwarp

# PhysX physics. Starts Isaac Sim.
uv run isaaclab train --rl_library rsl_rl --task Isaac-Cartpole \
    --num_envs 64 --max_iterations 5 physics=isaacsim_physx
```

The first Isaac Sim launch is slow while it builds caches. It also asks you
to accept the NVIDIA Omniverse license (EULA): read it and accept it yourself.
Don't set `OMNI_KIT_ACCEPT_EULA` in shared config to skip the prompt for
others.

## Comparing against mjlab

Isaac Lab 3.0 can run the same task on different physics engines. That lets
us separate two questions:

- **mjlab vs Isaac Lab as frameworks:** run Isaac Lab with
  `physics=newton_mjwarp`. Both use MuJoCo Warp 3.11 and RSL-RL 5.4, so most
  differences come from the frameworks themselves.
- **MuJoCo vs PhysX as physics engines:** run the same Isaac Lab task with
  `physics=isaacsim_physx`. A policy that works in both is more likely to work
  on the real robot.

## Notes on `pyproject.toml`

The lockfile is Linux x86_64 only. Two settings make it resolve, and both are
explained in comments: `opencv-python-headless-noffmpeg` is listed as a
direct dependency so it comes from NVIDIA's index, and a `pywin32` override
makes the lockfile resolvable from a Mac.

## What will go here

- `src/th_isaaclab/`: our robot configs and tasks, matching the mjlab ones.
  The `isaaclab` command finds tasks from installed packages through the
  `isaaclab.tasks` entry point, so ours will show up next to the built-in ones.
