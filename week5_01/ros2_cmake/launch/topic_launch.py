from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_cmake',
            namespace='ros2_cmake',
            executable='publisher',
            name='ex_pub'
        ),
        Node(
            package='ros2_cmake',
            namespace='ros2_cmake',
            executable='subscriber',
            name='ex_sub'
        ),
    ])