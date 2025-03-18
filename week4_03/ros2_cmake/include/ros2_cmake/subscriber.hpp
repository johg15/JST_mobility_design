#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

class StringSubscriber : public rclcpp::Node
{
  public:
    StringSubscriber(std::string node_name, std::string topic_name)
    : Node(node_name) {subscription_ = this->create_subscription<std_msgs::msg::String>(
      topic_name, 10, std::bind(&StringSubscriber::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::String & msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

