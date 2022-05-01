FROM osrf/ros:galactic-desktop

SHELL ["/bin/bash", "-c"]

# Install ROS 2 deppendencies (Cyclone DDS)
RUN sudo apt update && \
    sudo apt install -y \
    ros-galactic-rmw-cyclonedds-cpp \
    ros-galactic-navigation2 \
    ros-galactic-nav2-bringup \
    ros-galactic-slam-toolbox ros-galactic-nav2-amcl \
    ros-galactic-rosbridge-suite

RUN sudo rm -rf /var/lib/apt/lists/*

COPY cyclonedds.xml /
COPY ros_entrypoint.sh /
COPY server-node/config /config
RUN chmod +x /ros_entrypoint.sh

ENV CYCLONEDDS_URI=file:///cyclonedds.xml
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

ENTRYPOINT ["/ros_entrypoint.sh"]   

CMD ["bash", "-c", "ros2 run rosbridge_server rosbridge_websocket & \
                ros2 launch nav2_bringup bringup_launch.py \
                params_file:=/config/nav2_params.yaml map:=/config/map.yaml"]
