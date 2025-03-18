import sys
from ros2_interface.srv import ExCustomSrv
import rclpy
from rclpy.node import Node

class CustomClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(ExCustomSrv, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = ExCustomSrv.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    custom_client = CustomClientAsync()
    future = custom_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(custom_client, future)
    response = future.result()
    custom_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    custom_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()