from launch import LaunchDescription
from launch_ros.actions import Node

# yaml 파일에서 파라미터 읽어오기
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import PathJoinSubstitution

config_file = PathJoinSubstitution([get_package_share_directory('ros2_cmake'), 'config', 'param.yaml'])

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_cmake',
            namespace='ros2_cmake',
            executable='service_server',
            name='server'
        ),
        Node(
            package='ros2_cmake',
            namespace='ros2_cmake',
            executable='param_client',
            name='client',
            # parameters=[
            #     {"number1" : 1 },
            #     {"number2" : 2 }
            # ]
            parameters=[
                config_file
            ]
        ),
    ])