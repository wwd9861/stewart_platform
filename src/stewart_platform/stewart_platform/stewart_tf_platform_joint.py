from math import *

from geometry_msgs.msg import TransformStamped

import numpy as np

import rclpy
from rclpy.node import Node

from tf2_ros import TransformBroadcaster


class FramePublisher(Node):

    def __init__(self):
        super().__init__('platform_joint_frame')

        self.tf_broadcaster = TransformBroadcaster(self)
        self.create_timer(0.01, self.create_frame)

    def create_frame(self):
        t_1 = TransformStamped()
        t_2 = TransformStamped()
        t_3 = TransformStamped()
        t_4 = TransformStamped()
        t_5 = TransformStamped()
        t_6 = TransformStamped()


        t_1.header.frame_id = 'platform'
        t_1.child_frame_id = 'platform_joint_1'

        t_2.header.frame_id = 'platform'
        t_2.child_frame_id = 'platform_joint_2'

        t_3.header.frame_id = 'platform'
        t_3.child_frame_id = 'platform_joint_3'

        t_4.header.frame_id = 'platform'
        t_4.child_frame_id = 'platform_joint_4'

        t_5.header.frame_id = 'platform'
        t_5.child_frame_id = 'platform_joint_5'

        t_6.header.frame_id = 'platform'
        t_6.child_frame_id = 'platform_joint_6'

        t_1.transform.translation.x = 0.01717
        t_1.transform.translation.y = -0.020098
        t_1.transform.translation.z = -0.0025

        t_2.transform.translation.x = 0.01717
        t_2.transform.translation.y = 0.020098
        t_2.transform.translation.z = -0.0025

        t_3.transform.translation.x = 0.008585
        t_3.transform.translation.y = 0.024919
        t_3.transform.translation.z = -0.0025

        t_4.transform.translation.x = -0.02599
        t_4.transform.translation.y = 0.004821
        t_4.transform.translation.z = -0.0025

        t_5.transform.translation.x = -0.02599
        t_5.transform.translation.y = -0.004821
        t_5.transform.translation.z = -0.0025

        t_6.transform.translation.x = 0.008585
        t_6.transform.translation.y = -0.024919
        t_6.transform.translation.z = -0.0025


        t_1.transform.rotation.x = 0.0
        t_1.transform.rotation.y = 0.0
        t_1.transform.rotation.z = 0.0
        t_1.transform.rotation.w = 1.0

        t_2.transform.rotation.x = 0.0
        t_2.transform.rotation.y = 0.0
        t_2.transform.rotation.z = 0.0
        t_2.transform.rotation.w = 1.0

        t_3.transform.rotation.x = 0.0
        t_3.transform.rotation.y = 0.0
        t_3.transform.rotation.z = 0.0
        t_3.transform.rotation.w = 1.0
        
        t_4.transform.rotation.x = 0.0
        t_4.transform.rotation.y = 0.0
        t_4.transform.rotation.z = 0.0
        t_4.transform.rotation.w = 1.0

        t_5.transform.rotation.x = 0.0
        t_5.transform.rotation.y = 0.0
        t_5.transform.rotation.z = 0.0
        t_5.transform.rotation.w = 1.0

        t_6.transform.rotation.x = 0.0
        t_6.transform.rotation.y = 0.0
        t_6.transform.rotation.z = 0.0
        t_6.transform.rotation.w = 1.0

        t_1.header.stamp = self.get_clock().now().to_msg()
        self.tf_broadcaster.sendTransform(t_1)
        t_2.header.stamp = self.get_clock().now().to_msg()
        self.tf_broadcaster.sendTransform(t_2)
        t_3.header.stamp = self.get_clock().now().to_msg()
        self.tf_broadcaster.sendTransform(t_3)
        t_4.header.stamp = self.get_clock().now().to_msg()
        self.tf_broadcaster.sendTransform(t_4)
        t_5.header.stamp = self.get_clock().now().to_msg()
        self.tf_broadcaster.sendTransform(t_5)
        t_6.header.stamp = self.get_clock().now().to_msg()
        self.tf_broadcaster.sendTransform(t_6)


def main():
    rclpy.init()
    node = FramePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
