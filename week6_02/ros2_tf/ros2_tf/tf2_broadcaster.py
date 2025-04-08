from geometry_msgs.msg import TransformStamped
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster
from turtlesim.msg import Pose
from tf_transformations import quaternion_from_euler

class DyrosBroadcaster(Node):
   def __init__(self):
       super().__init__("tf2_broadcaster")

       self.turtlename = self.declare_parameter(
           'turtlename', 'turtle'
       ).get_parameter_value().string_value

       self.broadcaster = TransformBroadcaster(self)

       self.subscription = self.create_subscription(
           Pose,
           f'/{self.turtlename}/pose',
           self.handle_turtle_pose,
           1
       )
       self.subscription

   def handle_turtle_pose(self, msg):
       t = TransformStamped()
       t.header.stamp = self.get_clock().now().to_msg()
       t.header.frame_id = 'world'
       t.child_frame_id = self.turtlename

       t.transform.translation.x = msg.x
       t.transform.translation.y = msg.y
       t.transform.translation.z = 0.0


       quat = quaternion_from_euler(0, 0, msg.theta)
       t.transform.rotation.x = quat[0]
       t.transform.rotation.y = quat[1]
       t.transform.rotation.z = quat[2]
       t.transform.rotation.w = quat[3]

       self.broadcaster.sendTransform(t)

def main():
   rclpy.init()
   node = DyrosBroadcaster()
   try:
       rclpy.spin(node)
   except KeyboardInterrupt:
       pass
   rclpy.shutdown()


if __name__ == '__main__':
   main()


