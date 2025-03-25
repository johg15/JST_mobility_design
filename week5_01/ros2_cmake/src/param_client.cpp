#include "rclcpp/rclcpp.hpp"
#include "ros2_interface/srv/ex_custom_srv.hpp"
#include <chrono>
#include <cstdlib>
#include <memory>

using namespace std::chrono_literals;

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    std::shared_ptr<rclcpp::Node> node = rclcpp::Node::make_shared("param_client");
    rclcpp::Client<ros2_interface::srv::ExCustomSrv>::SharedPtr client =
        node->create_client<ros2_interface::srv::ExCustomSrv>("add_two_ints");

    const int invalid_value = std::numeric_limits<int>::min(); // 특수한 기본값(유효하지 않은 값으로 고려)
    int num1 = invalid_value;
    int num2 = invalid_value;
    std::string param_name1 = "number1";
    std::string param_name2 = "number2";

    // 파라미터 선언
    node->declare_parameter(param_name1,rclcpp::PARAMETER_INTEGER);
    node->declare_parameter(param_name2, rclcpp::PARAMETER_INTEGER); 


    // 파라미터 값 얻기 (number1)
    if (!node->get_parameter(param_name1, num1)) {
        RCLCPP_WARN(node->get_logger(), "Parameter '%s' not found, using default invalid value", param_name1.c_str());
    }
    
    // 파라미터 값 얻기 (number2)
    if (!node->get_parameter(param_name2, num2)) {
        RCLCPP_WARN(node->get_logger(), "Parameter '%s' not found, using default invalid value", param_name2.c_str());
    }

    // 유효성 검사
    // 두 숫자 파라미터를 모두 얻었는지 확인
    if (num1 == invalid_value || num2 == invalid_value) {
        RCLCPP_ERROR(node->get_logger(), "Invalid parameters detected. num1 = %d, num2 = %d. Check your parameter settings.", num1, num2);
        rclcpp::shutdown();
        return 1;
    }

    auto request = std::make_shared<ros2_interface::srv::ExCustomSrv::Request>();
    request->a = num1;
    request->b = num2;


    while (!client->wait_for_service(1s)) {
        if (!rclcpp::ok()) {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Interrupted while waiting for the service. Exiting.");
        return 0;
        }
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "service not available, waiting again...");
    }

    auto result = client->async_send_request(request);
    // Wait for the result.
    if (rclcpp::spin_until_future_complete(node, result) ==
        rclcpp::FutureReturnCode::SUCCESS)
    {
        RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Sum: %ld", result.get()->sum);
    } else {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Failed to call service add_two_ints");
    }
    
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
