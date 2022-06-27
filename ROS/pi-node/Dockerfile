FROM arm64v8/ros:galactic
#FROM osrf/ros:galactic-desktop

SHELL ["/bin/bash", "-c"]

# Install ROS 2 deppendencies (Cyclone DDS)
RUN sudo apt update && \
    sudo apt install -y \
    ros-galactic-rmw-cyclonedds-cpp \
    python3-pip 

# Install Raspberry pi sensor drivers and packages
RUN sudo apt update && \
    sudo apt install -y \
    python3-smbus \
    gpsd gpsd-clients 

RUN sudo python3 -m pip install --upgrade pip && \
    pip install -U \
    rpi.gpio \
    mpu6050-raspberrypi \ 
    gpsd-py3 \
    pyserial \
    pynmea2 

# Install OpenCV
RUN sudo apt install -y ros-galactic-cv-bridge \
    ros-galactic-vision-opencv \
    python3-opencv \
    libopencv-dev

RUN sudo python3 -m pip install --upgrade pip && \
    pip install -U \
    opencv-python-headless

# GPS related stuff 
RUN pip install 

RUN sudo rm -rf /var/lib/apt/lists/*

WORKDIR /app

# build custom ROS 2 nodes
COPY ros2_ws ros2_ws/
RUN cd ros2_ws && \
    source /opt/ros/galactic/setup.bash && \
    colcon build

# Configure GPS driver
RUN sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
# RUN sudo gpsd /dev/serial1 -F /var/run/gpsd.sock

# Setup CycloneDDS (Only if using VPN)
COPY cyclonedds.xml /
ENV CYCLONEDDS_URI=file:///cyclonedds.xml
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

COPY ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh

RUN echo "source /opt/ros/galactic/setup.bash" >> ~/.bashrc && \
    echo "source /app/ros2_ws/install/setup.bash" >> ~/.bashrc && \
    source ~/.bashrc
    
ENTRYPOINT ["/ros_entrypoint.sh"]   
CMD ["bash"]