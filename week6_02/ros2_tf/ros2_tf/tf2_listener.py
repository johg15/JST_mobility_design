import math
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from turtlesim.srv import Spawn

class DyroosListener(Node):
   def __init__(self):
       super().__init__("tf2_listener")

       self.target_frame = self.declare_parameter(
           'target_frame', 'turtle1'
       ).get_parameter_value().string_value

       self.buffer = Buffer()
       self.listener = TransformListener(self.buffer, self)

       self.spawner = self.create_client(Spawn, 'spawn')

       self.turtle_spawning_service_ready = False
       self.turtle_spawned = False

       self.turtle_vel = self.create_publisher(Twist,
                               'turtle2/cmd_vel', 1)
      
       self.timer = self.create_timer(1.0, self.on_timer)

   def on_timer(self):
       from_frame = self.target_frame
       to_frame = 'turtle2'

       if self.turtle_spawning_service_ready:
           if self.turtle_spawned:
               try:
                   t = self.buffer.lookup_transform(
                       to_frame,
                       from_frame,
                       rclpy.time.Time()
                   )
               except TransformException as ex:
                   self.get_logger.info(
                       f'Could not transform {to_frame} to {from_frame}: {ex}')
                   return
              
               msg = Twist()
               msg.angular.z  = 1.0*math.atan2(t.transform.translation.y,
                                               t.transform.translation.x)
               msg.linear.x = 0.5*math.sqrt(t.transform.translation.x**2+
                                           t.transform.translation.y**2)

               self.turtle_vel.publish(msg)

           else:
               if self.result.done():
                   self.get_logger().info(
                       f'Successfully spawned {self.result.result().name}'
                   )
                   self.turtle_spawned = True
               else:
                   self.get_logger().info('Spawned is not fisnished')
                  
       else:
           if self.spawner.service_is_ready():
               req = Spawn.Request()
               req.name = "turtle2"
               req.x, req.y, req.theta = float(4), float(2), float(0)

               self.result = self.spawner.call_async(req)
               self.turtle_spawning_service_ready = True
           else:
               self.get_logger().info('Service is not ready')

def main():
   rclpy.init()
   node = DyroosListener()
   try:
       rclpy.spin(node)
   except KeyboardInterrupt:
       pass

   rclpy.shutdown()

if __name__ == "__main__":
   main()
              


