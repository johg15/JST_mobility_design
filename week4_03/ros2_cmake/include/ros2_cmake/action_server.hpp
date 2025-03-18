#ifndef ROS2_CMAKE__ACTION_SERVER_HPP_ 
#define ROS2_CMAKE__ACTION_SERVER_HPP_

#include <functional>
#include <memory>
#include <thread>
#include "ros2_interface/action/fibonacci.hpp"
#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"

using Fibonacci = ros2_interface::action::Fibonacci;
using GoalHandleFibonacci = rclcpp_action::ServerGoalHandle<Fibonacci>;

class FibonacciActionServer : public rclcpp::Node
{
public:
  explicit FibonacciActionServer(const rclcpp::NodeOptions & options = rclcpp::NodeOptions());
  virtual ~FibonacciActionServer() = default;

private:
  rclcpp_action::Server<Fibonacci>::SharedPtr action_server_;
  rclcpp_action::GoalResponse handle_goal(
    const rclcpp_action::GoalUUID & uuid,
    std::shared_ptr<const Fibonacci::Goal> goal);
  rclcpp_action::CancelResponse handle_cancel(
    const std::shared_ptr<GoalHandleFibonacci> goal_handle);

  void handle_accepted(const std::shared_ptr<GoalHandleFibonacci> goal_handle);
  void execute(const std::shared_ptr<GoalHandleFibonacci> goal_handle);

};  // class FibonacciActionServer

#endif // ROS2_CMAKE__ACTION_SERVER_HPP_