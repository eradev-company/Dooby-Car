import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='dooby_simulation').find('dooby_simulation')
    default_model_path = os.path.join(pkg_share, 'src/description/dooby_bot.urdf')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/config.rviz')
    world_path=os.path.join(pkg_share, 'world/my_world.sdf')
    
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )
    
    static_publisher = launch_ros.actions.Node(
    	package='tf2_ros', 
    	executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0','1', 'odom', 'map']
    )

    

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                            description='Flag to enable joint_state_publisher_gui'),
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='True',
                                            description='Flag to enable use_sim_time'),
        #launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path], output='screen'),
        static_publisher,
        rviz_node
    ])
