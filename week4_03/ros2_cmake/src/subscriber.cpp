#include "ros2_cmake/subscriber.hpp"

int main(int argc, char * argv[]) {
    std::string node_name = "ex_sub_node";
    std::string topic_name = "/ex_message";
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<StringSubscriber>(node_name, topic_name));
    rclcpp::shutdown();
    return 0;
}