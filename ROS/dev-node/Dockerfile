FROM tiryoh/ros2-desktop-vnc:galactic

SHELL ["/bin/bash", "-c"]

# Install ROS 2 deppendencies (Cyclone DDS)
RUN sudo apt update && \
    sudo apt install -y \
    ros-galactic-rmw-cyclonedds-cpp \
    ros-galactic-joint-state-publisher-gui \
    ros-galactic-xacro \
    ros-galactic-robot-localization \
    ros-galactic-gazebo-ros-pkgs 

# Install OpenCV
RUN sudo apt update && \
    sudo apt install -y python3-pip libopencv-dev python3-opencv \
    ros-galactic-vision-opencv

RUN sudo python3 -m pip install --upgrade pip && \
    pip install -U opencv-python-headless

# Install ROS Web Bridge
RUN sudo apt install -y ros-galactic-cv-bridge 

# Install Nav2 stack
RUN sudo apt install -y ros-galactic-navigation2 \
    ros-galactic-nav2-bringup \
    ros-galactic-slam-toolbox ros-galactic-nav2-amcl 

RUN sudo rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Set up CycloneDDS (comment this out if local network setup)
COPY cyclonedds.xml /
ENV CYCLONEDDS_URI=file:///cyclonedds.xml
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Copy custom ROS 2 nodes
COPY ros2_ws ros2_ws/
RUN chown -R ubuntu ros2_ws/ 

USER ubuntu

# build custom ROS 2 nodes
RUN cd ros2_ws && \
    source /opt/ros/galactic/setup.bash && \
    colcon build

RUN echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc && \
    echo "source /app/ros2_ws/install/setup.bash" >> ~/.bashrc && \
    source ~/.bashrc

USER root

CMD ["bash"]