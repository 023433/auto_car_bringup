from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import xacro
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
  share_dir = get_package_share_directory('auto_car_description')

  xacro_file = os.path.join(share_dir, 'urdf', 'AutoCar.xacro')
  robot_description_config = xacro.process_file(xacro_file)
  robot_urdf = robot_description_config.toxml()

  core_node = Node(
    package='auto_car_core',
    executable='autocar',
  )

  robot_state_publisher_node = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    name='robot_state_publisher',
    parameters=[
      {'robot_description': robot_urdf}
    ]
  )

  joint_state_publisher_node = Node(
    package='joint_state_publisher',
    executable='joint_state_publisher',
    name='joint_state_publisher'
  )

  return LaunchDescription([
    core_node,
    robot_state_publisher_node,
    joint_state_publisher_node,
  ])
