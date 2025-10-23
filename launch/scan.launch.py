from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

import os

def generate_launch_description():
    # Declare arguments
    declared_arguments = []
 

    pkg_trxbewi_scan = get_package_share_directory("trxbewi_scan")
    params_file = os.path.join(pkg_trxbewi_scan, "config", "config.yaml")
    
    scan_node = Node(
        package='rplidar_ros',
        executable='rplidar_node',
        name='scan_a2m12_node',
        parameters=[params_file],
    )

    return LaunchDescription([scan_node])