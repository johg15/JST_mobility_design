#include "ros2_cmake/publisher.hpp"

int main(int argc, char * argv[]) {
    std::string node_name = "ex_pub_node";
    std::string topic_name = "/ex_message";
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<StringPublisher>(node_name, topic_name));
    rclcpp::shutdown();
    return 0;
}