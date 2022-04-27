FROM osrf/ros:galactic-desktop

SHELL ["/bin/bash", "-c"]

# Install ROS 2 deppendencies (Cyclone DDS)
RUN sudo apt update && \
    sudo apt install -y \
    ros-galactic-rmw-cyclonedds-cpp \
    ros-galactic-joint-state-publisher-gui \
    ros-galactic-xacro \
    ros-galactic-robot-localization \
    ros-galactic-gazebo-ros-pkgs \
    ros-galactic-navigation2 \
    ros-galactic-nav2-bringup \
    ros-galactic-slam-toolbox ros-galactic-nav2-amcl \
    ros-galactic-mapviz \
    ros-galactic-mapviz-plugins \
    ros-galactic-tile-map \
    ros-galactic-multires-image 
RUN sudo rm -rf /var/lib/apt/lists/*

WORKDIR /app

# build custom ROS 2 nodes
COPY ros2_ws ros2_ws/
RUN cd ros2_ws && \
    source /opt/ros/galactic/setup.bash && \
    colcon build

COPY server-node/cyclonedds.xml .
COPY server-node/ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]   
CMD ["bash"]