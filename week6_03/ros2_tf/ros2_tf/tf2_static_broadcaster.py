import sys
from geometry_msgs.msg import TransformStamped
import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from tf_transformations import quaternion_from_euler
class DyrosStaticBroadcaster(Node):
   def __init__(self, tf):
       super().__init__('tf2_static_broadcaster')
       self.broadcaster = StaticTransformBroadcaster(self)
       self.make_transform(tf)

   def make_transform(self, tf):
       t = TransformStamped()
       t.header.stamp = self.get_clock().now().to_msg()
       t.header.frame_id = 'world'
       t.child_frame_id = tf[1]

       t.transform.translation.x = float(tf[2])
       t.transform.translation.y = float(tf[3])
       t.transform.translation.z = float(tf[4])

       quat = quaternion_from_euler(float(tf[5]), float(tf[6]), float(tf[7]))
       t.transform.rotation.x = quat[0]
       t.transform.rotation.y = quat[1]
       t.transform.rotation.z = quat[2]
       t.transform.rotation.w = quat[3]

       self.broadcaster.sendTransform(t)

def main():
   args = sys.argv
   logger = rclpy.logging.get_logger('logger')
   if len(args) < 8:
       logger.info("Invalid number of parameters. Usage: \n"
       '$ ros2 run tf2_static_broadcaster.py'
       'child_frame_name x y z roll pitch yaw')
       sys.exit(0)
   else:
       if args[1] == 'world':
           logger.info('Your static turtle name cannot be "world"')
           sys.exit(0)
   rclpy.init()
   node = DyrosStaticBroadcaster(args)
   try:
       rclpy.spin(node)
   except KeyboardInterrupt:
       pass
   rclpy.shutdown()
if __name__ == "__main__":
   main()

