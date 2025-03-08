from math import *
import sys
from geometry_msgs.msg import TransformStamped
import numpy as np
import rclpy
from rclpy.node import Node
from tf2_ros import TransformBroadcaster


def quaternion_from_euler(ai, aj, ak):
    ai /= 2.0
    aj /= 2.0
    ak /= 2.0
    ci = cos(ai)
    si = sin(ai)
    cj = cos(aj)
    sj = sin(aj)
    ck = cos(ak)
    sk = sin(ak)
    cc = ci*ck
    cs = ci*sk
    sc = si*ck
    ss = si*sk

    q = np.empty((4, ))
    q[0] = cj*sc - sj*cs
    q[1] = cj*ss + sj*cc
    q[2] = cj*cs - sj*sc
    q[3] = cj*cc + sj*ss

    return q


class FramePublisher(Node):

    def __init__(self):
        super().__init__('servo_frame')

        self.tf_broadcaster = TransformBroadcaster(self)

        self.create_timer(0.01, self.create_frame)

    def create_frame(self):
        t_1 = TransformStamped()
        t_2 = TransformStamped()
        t_3 = TransformStamped()
        t_4 = TransformStamped()
        t_5 = TransformStamped()
        t_6 = TransformStamped()

        
        t_1.header.frame_id = 'world'
        t_1.child_frame_id = 'servo_1'

        t_2.header.frame_id = 'world'
        t_2.child_frame_id = 'servo_2'

        t_3.header.frame_id = 'world'
        t_3.child_frame_id = 'servo_3'

        t_4.header.frame_id = 'world'
        t_4.child_frame_id = 'servo_4'

        t_5.header.frame_id = 'world'
        t_5.child_frame_id = 'servo_5'

        t_6.header.frame_id = 'world'
        t_6.child_frame_id = 'servo_6'

        t_1.transform.translation.x = 0.047
        t_1.transform.translation.y = -0.0150
        t_1.transform.translation.z = 0.0110

        t_2.transform.translation.x = 0.0470
        t_2.transform.translation.y = 0.0150
        t_2.transform.translation.z = 0.0110

        t_3.transform.translation.x = -0.01051
        t_3.transform.translation.y = 0.048203
        t_3.transform.translation.z = 0.0110

        t_4.transform.translation.x = -0.03649
        t_4.transform.translation.y = 0.033203
        t_4.transform.translation.z = 0.0110

        t_5.transform.translation.x = -0.03649
        t_5.transform.translation.y = -0.033203
        t_5.transform.translation.z = 0.0110

        t_6.transform.translation.x = -0.01051
        t_6.transform.translation.y = -0.048203
        t_6.transform.translation.z = 0.0110



        q_1 = quaternion_from_euler(0.0, 0.0, 0.0)
        q_2 = quaternion_from_euler(0.0, 0.0, 0.0)
        q_3 = quaternion_from_euler(0.0, 0.0, pi*2/3)
        q_4 = quaternion_from_euler(0.0, 0.0, pi*2/3)
        q_5 = quaternion_from_euler(0.0, 0.0, pi*4/3)
        q_6 = quaternion_from_euler(0.0, 0.0, pi*4/3)



        t_1.transform.rotation.x = q_1[0]
        t_1.transform.rotation.y = q_1[1]
        t_1.transform.rotation.z = q_1[2]
        t_1.transform.rotation.w = q_1[3]
        
        t_2.transform.rotation.x = q_2[0]
        t_2.transform.rotation.y = q_2[1]
        t_2.transform.rotation.z = q_2[2]
        t_2.transform.rotation.w = q_2[3]

        t_3.transform.rotation.x = q_3[0]
        t_3.transform.rotation.y = q_3[1]
        t_3.transform.rotation.z = q_3[2]
        t_3.transform.rotation.w = q_3[3]

        t_4.transform.rotation.x = q_4[0]
        t_4.transform.rotation.y = q_4[1]
        t_4.transform.rotation.z = q_4[2]
        t_4.transform.rotation.w = q_4[3]

        t_5.transform.rotation.x = q_5[0]
        t_5.transform.rotation.y = q_5[1]
        t_5.transform.rotation.z = q_5[2]
        t_5.transform.rotation.w = q_5[3]

        t_6.transform.rotation.x = q_6[0]
        t_6.transform.rotation.y = q_6[1]
        t_6.transform.rotation.z = q_6[2]
        t_6.transform.rotation.w = q_6[3]


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
