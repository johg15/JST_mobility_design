import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class StringPublisher(Node):

    def __init__(self, node_name, topic_name):
        super().__init__(node_name)
        self.publisher_ = self.create_publisher(String, topic_name, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    node_name = "ex_pub_node_py"
    topic_name = "/ex_message_py"

    string_publisher = StringPublisher(node_name, topic_name)

    rclpy.spin(string_publisher)

    string_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()