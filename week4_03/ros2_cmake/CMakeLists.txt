cmake_minimum_required(VERSION 3.8)
project(ros2_cmake)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# service 
find_package(ros2_interface REQUIRED)

include_directories(include)

# topic - publisher
add_executable(publisher src/publisher.cpp)
ament_target_dependencies(publisher rclcpp std_msgs)

# topic - subscriber
add_executable(subscriber src/subscriber.cpp)
ament_target_dependencies(subscriber rclcpp std_msgs)

# service - server
add_executable(service_server src/service_server.cpp)
ament_target_dependencies(service_server rclcpp ros2_interface)

# service - client
add_executable(service_client src/service_client.cpp)
ament_target_dependencies(service_client rclcpp ros2_interface)


# action

find_package(rclcpp_action REQUIRED)

# action - server
add_executable(action_server src/action_server.cpp)
ament_target_dependencies(action_server rclcpp ros2_interface rclcpp_action)

# action - client
add_executable(action_client src/action_client.cpp)
ament_target_dependencies(action_client rclcpp ros2_interface rclcpp_action)


install(TARGETS
  # topic
  publisher
  subscriber
  
  # service 
  service_server
  service_client

  #action
  action_server
  action_client

  DESTINATION lib/${PROJECT_NAME})


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
