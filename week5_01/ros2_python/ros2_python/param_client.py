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

        # 파라미터 선언
        self.declare_parameter('number1', 0)
        self.declare_parameter('number2', 0)


    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    custom_client = CustomClientAsync()
    
    # 파라미터 값 읽기
    num1 = custom_client.get_parameter('number1').value
    num2 = custom_client.get_parameter('number2').value

    future = custom_client.send_request(int(num1), int(num2))
    rclpy.spin_until_future_complete(custom_client, future)

    response = future.result()
    custom_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(num1), int(num2), response.sum))

    custom_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()