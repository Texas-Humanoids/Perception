# BerkeleyBot

The stock [Berkeley Humanoid Lite](https://github.com/HybridRobotics/berkeley-humanoid-lite),
unmodified hardware. We use it as a known-good robot to test our training and
deployment pipeline before our own robots are ready.

| File | Model |
| --- | --- |
| `mjcf/berkeley_humanoid_lite.xml` | full robot: 22 actuated joints (legs + arms) |
| `mjcf/berkeley_humanoid_lite_biped.xml` | legs only: 12 actuated joints |
| `mjcf/bhl_scene.xml`, `mjcf/bhl_biped_scene.xml` | the above, plus a floor and lights for viewing |
| `urdf/berkeley_humanoid_lite.urdf`, `urdf/berkeley_humanoid_lite_biped.urdf` | the same two models for ROS |

To look at it in MuJoCo:

```bash
python -m mujoco.viewer --mjcf=mjcf/bhl_scene.xml
```

## Source and license

Copied from [HybridRobotics/Berkeley-Humanoid-Lite-Assets](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite-Assets)
at commit `fc90fedd008b1e56a22e3c5221548d6b24f49707`
(`data/robots/berkeley_humanoid/berkeley_humanoid_lite/`).

These files are licensed under **CC BY-SA 4.0** (see [`LICENSE`](LICENSE)),
not the MIT license used by the rest of this repo. If you change them, the
changed files must stay CC BY-SA 4.0.

Changes from upstream:

- **MJCF:** fixed mesh paths so the files load from this folder
  (`meshdir="assets"` → `meshdir="../meshes"`, and dropped the `merged/`
  prefix from mesh file names). Nothing else changed.
- **URDF:** unchanged. Mesh paths are still `package://../meshes/...`, which
  ROS can't resolve yet. They'll be fixed when `th_description` becomes a
  real ROS package.
- Not copied: USD files (Isaac Sim only), OpenSCAD sources, and the
  onshape-to-robot export configs.
