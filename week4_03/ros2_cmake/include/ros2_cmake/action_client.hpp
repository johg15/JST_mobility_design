#ifndef ROS2_CMAKE__ACTION_CLIENT_HPP_ 
#define ROS2_CMAKE__ACTION_CLIENT_HPP_

#include <functional>
#include <future>
#include <memory>
#include <string>
#include <sstream>

#include "ros2_interface/action/fibonacci.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"

using Fibonacci = ros2_interface::action::Fibonacci;
using GoalHandleFibonacci = rclcpp_action::ClientGoalHandle<Fibonacci>;


class FibonacciActionClient : public rclcpp::Node
{
public:

    explicit FibonacciActionClient(const rclcpp::NodeOptions & options = rclcpp::NodeOptions());
    virtual ~FibonacciActionClient() =default;


  void send_goal();

private:
  rclcpp_action::Client<Fibonacci>::SharedPtr client_ptr_;
  rclcpp::TimerBase::SharedPtr timer_;

  void goal_response_callback(const GoalHandleFibonacci::SharedPtr & goal_handle);


  void feedback_callback(
    GoalHandleFibonacci::SharedPtr,
    const std::shared_ptr<const Fibonacci::Feedback> feedback);


  void result_callback(const GoalHandleFibonacci::WrappedResult & result);

};  // class FibonacciActionClient

#endif // ROS2_CMAKE__ACTION_SERVER_HPP_


