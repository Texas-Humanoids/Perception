# humanoid_ws

Software for the Texas Humanoids robot, a humanoid based on the
[Berkeley Humanoid Lite](https://github.com/HybridRobotics/berkeley-humanoid-lite),
built on **ROS 2 Jazzy**.

This repo is a ROS 2 workspace. Right now it only has the folder layout;
code will be added in later pull requests.

## Repository layout

```
humanoid_ws/
├── src/                    ROS 2 packages
│   ├── th_description/     robot model (URDF, meshes)
│   ├── th_bringup/         launch files and config that start the robot
│   ├── robstride_driver/   talks to the RobStride motors over CAN
│   ├── th_hardware/        connects ROS controllers to the motors
│   ├── th_controllers/     custom controllers (RL walking policy)
│   ├── th_sensors/         IMU, camera, and other sensor drivers
│   └── th_perception/      GPU perception with Isaac ROS (optional)
├── firmware/               microcontroller code for future custom motors
├── policies/               trained walking policies
└── tools/                  calibration and setup scripts
```

`th_` = Texas Humanoids. It marks packages we wrote, so they're easy to tell
apart from third-party ones.

Each folder has a README describing what will go in it.
