from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='dooby_interface',
            executable='dooby_interface',
            name='interface',
            parameters=[{'use_sim_time': True}]
        ),
        Node(
            package='dooby_interface',
            executable='dooby_imu',
            name='imu',
            parameters=[{'use_sim_time': True}]
        ),

        Node(
            package='dooby_interface',
            executable='dooby_cam',
            name='cam',
            parameters=[{'use_sim_time': True}]
        ),
        # Node(
        #     package='dooby_interface',
        #     executable='dooby_gps',
        #     name='gps',
        #     parameters=[{'use_sim_time': True}]
        # )
    ])