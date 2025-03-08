import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        Node(
            package='stewart_platform',
            executable='stewart_tf_platform',
            name='stewart_tf_platform',
        ),
        Node(
            package='stewart_platform',
            executable='stewart_tf_platform_joint',
            name='stewart_tf_platform_joint',
        ),
        Node(
            package='stewart_platform',
            executable='stewart_tf_servo',
            name='stewart_tf_servo',
        ),
        Node(
            package='stewart_platform',
            executable='stewart_ik',
            name='stewart_ik',
        ),
    ])