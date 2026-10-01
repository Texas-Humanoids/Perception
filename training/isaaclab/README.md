# training/isaaclab

Policy training with [Isaac Lab](https://isaac-sim.github.io/IsaacLab/)
2.3.2 on Isaac Sim 5.1. See [`../README.md`](../README.md) for how this fits
with the other simulator.

These are the same versions the
[Berkeley Humanoid Lite](https://github.com/HybridRobotics/berkeley-humanoid-lite)
repo uses, so its official Isaac Lab tasks are a known-good baseline to
compare against.

## Requirements

- Linux x86_64 (Ubuntu 22.04 or newer). **There is no macOS support.**
- An NVIDIA RTX GPU. See the
  [Isaac Sim requirements](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/requirements.html).

## Setup

```bash
cd training/isaaclab
uv sync
```

This is a large download. Then check that Isaac Sim starts:

```bash
uv run python -c "from isaaclab.app import AppLauncher; AppLauncher(headless=True).app.close()"
```

The first launch is slow while Isaac Sim builds its caches. It also asks you
to accept the NVIDIA Omniverse license (EULA): read it and accept it yourself.
Don't set `OMNI_KIT_ACCEPT_EULA` in shared config to skip the prompt for
others.

## Notes on the lockfile

`uv.lock` is for Linux x86_64 only. You can update it from a Mac, but
`pyproject.toml` needs two workarounds for that (an `exclude-newer` date and
a `pywin32` override). Both are explained in comments there.

## What will go here

- `src/th_isaaclab/`: our robot configs and task environments, matching the
  mjlab ones so we can compare the two simulators on the same task
