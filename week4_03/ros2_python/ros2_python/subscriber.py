import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringSubscriber(Node):

    def __init__(self, node_name, topic_name):
        super().__init__(node_name)
        self.subscription = self.create_subscription(
            String,
            topic_name,
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node_name = "ex_sub_node_py"
    topic_name = "/ex_message_py"

    string_subscriber = StringSubscriber(node_name, topic_name)

    rclpy.spin(string_subscriber)

    string_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()