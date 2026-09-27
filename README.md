# Isaac ROS workspace

```bash
export LOCAL_UID=$(id -u) LOCAL_GID=$(id -g)

docker compose --profile cpu build     # or
docker compose --profile gpu build  

docker compose --profile cpu run --rm cpu bash
docker compose --profile gpu run --rm gpu bash
```

Inside either container:

```bash
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
```
On GPU hosts, install the NVIDIA Container Toolkit before using the GPU profile.

Make sure to open this folder in VS Code with the Remote - Containers extension. The `devcontainer.json` file will automatically build and open the container for you. You can also use the `Remote-Containers: Reopen in Container` command from the Command Palette.