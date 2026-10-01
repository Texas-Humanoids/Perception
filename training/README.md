# training

Trains our walking policies in simulation with
[mjlab](https://github.com/mujocolab/mjlab), then exports them as `.onnx`
files to [`../policies/`](../policies/).

This folder is a standalone Python project managed with
[uv](https://docs.astral.sh/uv/). It is **not** a ROS package: the
`COLCON_IGNORE` file tells `colcon build` to skip it, and it uses its own
virtual environment rather than the ROS system Python.

## Why it lives in this repo

The policy and the controller that runs it on the robot (`th_controllers`)
must agree on joint order, observations, action scaling, default pose, and
gains. Keeping training here means a change to any of those updates both
sides in the same pull request.

## Setup

```bash
cd training
uv sync
uv run python -c "import mjlab, th_training"
```

macOS works for small CPU experiments. Real training runs should use Linux
with an NVIDIA GPU.

## What will go here

- `src/th_training/`: our robot config and task environments (standing,
  velocity tracking), plus ONNX export
- `tests/`: quick CPU checks that the environments build and step

The robot model will be loaded from `../src/th_description`, not copied
here, so there is one source of truth for it.

Training outputs (`logs/`, checkpoints, `wandb/`) are ignored by git. Only the
policies we actually deploy get committed, to `../policies/`.
