#FROM arm64v8/ros:galactic
FROM osrf/ros:galactic-desktop

SHELL ["/bin/bash", "-c"]

# Install ROS 2 deppendencies (Cyclone DDS)
RUN sudo apt update && \
    sudo apt install -y \
    ros-galactic-rmw-cyclonedds-cpp 
RUN sudo rm -rf /var/lib/apt/lists/*

WORKDIR /app

# build custom ROS 2 nodes
COPY ros2_ws ros2_ws/
RUN cd ros2_ws && \
    source /opt/ros/galactic/setup.bash && \
    colcon build

COPY cyclonedds.xml /
COPY ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh

ENV CYCLONEDDS_URI=file:///cyclonedds.xml
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

ENTRYPOINT ["/ros_entrypoint.sh"]   
CMD ["bash"]