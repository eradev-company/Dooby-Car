import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='dooby_simulation').find('dooby_simulation')
    default_model_path = os.path.join(pkg_share, 'src/description/dooby_bot.urdf')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/config.rviz')
    world_path=os.path.join(pkg_share, 'world/my_world.sdf')
    
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
    )

    robot_localization_node = launch_ros.actions.Node(
         package='robot_localization',
         executable='ekf_node',
         name='ekf_filter_node',
         output='screen',
         parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    robot_map_node = launch_ros.actions.Node(
         package='robot_localization',
         executable='ekf_node',
         name='ekf_map_node',
         output='screen',
         parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    map_localization_node = launch_ros.actions.Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_map_node',
            output='screen',
            parameters=[os.path.join(pkg_share, 'config/ekf_map.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )
    
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )
    spawn_entity = launch_ros.actions.Node(
    	package='gazebo_ros', 
    	executable='spawn_entity.py',
        arguments=['-entity', 'dooby_bot', '-topic', 'robot_description'],
        output='screen'
    )

    static_pose = launch_ros.actions.Node(
    	package='tf2_ros', 
    	executable='static_transform_publisher',
        arguments=['0', '0', '0', '0', '0', '0','1', 'odom', 'map']
    )

    script = launch_ros.actions.Node(
            package='dooby_interface',
            executable='script',
            name='script',
            parameters=[{'use_sim_time': True}]
        )
    
    clock = launch_ros.actions.Node(
            package='dooby_interface',
            executable='clock',
            name='clock_publisher',
            parameters=[{'use_sim_time': True}]
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
        joint_state_publisher_node,
        robot_state_publisher_node,
        static_pose,
        #spawn_entity,
        #clock,
        robot_localization_node,
        #robot_map_node,
        rviz_node
    ])
