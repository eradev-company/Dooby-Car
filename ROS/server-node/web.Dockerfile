FROM osrf/ros:galactic-desktop

SHELL ["/bin/bash", "-c"]

# Install ROS 2 deppendencies (Cyclone DDS)
RUN sudo apt update && \
    sudo apt install -y \
    ros-galactic-rmw-cyclonedds-cpp 

# Install ROS Web Bridge
RUN sudo apt install -y ros-galactic-rosbridge-server

RUN sudo rm -rf /var/lib/apt/lists/*

# Setup CycloneDDS (Only if using VPN)
COPY cyclonedds.xml /
ENV CYCLONEDDS_URI=file:///cyclonedds.xml
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

RUN echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc && \
    source ~/.bashrc
    
CMD ["bash", "-c", "sleep 10 && ros2 run rosbridge_server rosbridge_websocket"]
