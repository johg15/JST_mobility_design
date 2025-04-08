from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
   return LaunchDescription([
       DeclareLaunchArgument(
           'target_frame', default_value='turtle1',
           description='Target frame name.'
       ),
       Node(
           package='turtlesim',
           executable='turtlesim_node',
           name='sim'
       ),
       Node(
           package='ros2_tf',
           executable="tf2_broadcaster",
           name="turtle1_tf2_broadcaster",
           parameters=[
               {'turtlename': 'turtle1'}
           ]
       ),
   ])


