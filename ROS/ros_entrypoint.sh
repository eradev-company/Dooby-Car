#!/bin/bash
set -e

source /opt/ros/galactic/setup.bash

# if /app/ros2_ws/install/setup.bash exists, source it
if [ -f /app/ros2_ws/install/setup.bash ]; then
  source /app/ros2_ws/install/setup.bash
fi

# wait for vpn to be connected
sleep 10

exec "$@"