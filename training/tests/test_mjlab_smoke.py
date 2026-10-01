"""Check that mjlab, MuJoCo Warp, and torch work together on CPU.

Uses mjlab's built-in cartpole so it doesn't depend on our robot model.
If this fails after an mjlab version bump, the problem is the toolchain,
not our tasks.
"""

import torch
from mjlab.envs import ManagerBasedRlEnv
from mjlab.tasks.registry import load_env_cfg


def test_cartpole_steps_on_cpu():
    cfg = load_env_cfg("Mjlab-Cartpole-Balance")
    cfg.scene.num_envs = 2
    cfg.seed = 0
    env = ManagerBasedRlEnv(cfg=cfg, device="cpu")
    try:
        obs, _ = env.reset()
        num_actions = env.action_manager.total_action_dim
        with torch.inference_mode():
            for _ in range(10):
                obs, reward, *_ = env.step(torch.zeros(2, num_actions))
        assert torch.isfinite(obs["actor"]).all()
        assert torch.isfinite(reward).all()
    finally:
        env.close()
