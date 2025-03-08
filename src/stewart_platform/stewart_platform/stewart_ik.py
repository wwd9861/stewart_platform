from math import atan2 
from numpy import *
import rclpy
from rclpy.node import Node

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from std_msgs.msg import Float64MultiArray



class FrameListener(Node):

    def __init__(self):
        super().__init__('turtle_tf2_frame_listener')

        # self.data = JointTrajectory()
        # self.data.header.frame_id="world"
        # self.data.joint_names=['revolute1', 'revolute2', 'revolute3','revolute4', 'revolute5', 'revolute6']
        # self.point = JointTrajectoryPoint()
        # self.publisher = self.create_publisher(JointTrajectory, '/set_joint_trajectory', 10)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.publisher = self.create_publisher(Float64MultiArray, 'ik_solution', 1)
        self.aa=Float64MultiArray()
        self.timer=self.create_timer(0.01, self.on_timer)

    def on_timer(self):
        l1=0.08
        l2=0.025
        
        try:
            t_1 = self.tf_buffer.lookup_transform('servo_1','platform_joint_1',rclpy.time.Time())
            x_1=t_1.transform.translation.x
            y_1=t_1.transform.translation.y
            z_1=t_1.transform.translation.z
            t_2 = self.tf_buffer.lookup_transform('servo_2','platform_joint_2',rclpy.time.Time())
            x_2=t_2.transform.translation.x
            y_2=t_2.transform.translation.y
            z_2=t_2.transform.translation.z
            t_3 = self.tf_buffer.lookup_transform('servo_3','platform_joint_3',rclpy.time.Time())
            x_3=t_3.transform.translation.x
            y_3=t_3.transform.translation.y
            z_3=t_3.transform.translation.z
            t_4 = self.tf_buffer.lookup_transform('servo_4','platform_joint_4',rclpy.time.Time())
            x_4=t_4.transform.translation.x
            y_4=t_4.transform.translation.y
            z_4=t_4.transform.translation.z
            t_5 = self.tf_buffer.lookup_transform('servo_5','platform_joint_5',rclpy.time.Time())
            x_5=t_5.transform.translation.x
            y_5=t_5.transform.translation.y
            z_5=t_5.transform.translation.z
            t_6 = self.tf_buffer.lookup_transform('servo_6','platform_joint_6',rclpy.time.Time())
            x_6=t_6.transform.translation.x
            y_6=t_6.transform.translation.y
            z_6=t_6.transform.translation.z

            theta_1=atan2(z_1,y_1)+arccos((x_1**2+y_1**2+z_1**2+l2**2-l1**2)/(2*l2*sqrt(z_1**2+y_1**2)))
            theta_2=atan2(z_2,y_2)-arccos((x_2**2+y_2**2+z_2**2+l2**2-l1**2)/(2*l2*sqrt(z_2**2+y_2**2)))
            theta_3=atan2(z_3,y_3)+arccos((x_3**2+y_3**2+z_3**2+l2**2-l1**2)/(2*l2*sqrt(z_3**2+y_3**2)))
            theta_4=atan2(z_4,y_4)-arccos((x_4**2+y_4**2+z_4**2+l2**2-l1**2)/(2*l2*sqrt(z_4**2+y_4**2)))
            theta_5=atan2(z_5,y_5)+arccos((x_5**2+y_5**2+z_5**2+l2**2-l1**2)/(2*l2*sqrt(z_5**2+y_5**2)))
            theta_6=atan2(z_6,y_6)-arccos((x_6**2+y_6**2+z_6**2+l2**2-l1**2)/(2*l2*sqrt(z_6**2+y_6**2)))

            self.aa.data = [-(pi-theta_1), theta_2,-(pi-theta_3), theta_4,-(pi-theta_5), theta_6]
            self.publisher.publish(self.aa)
            
            # print("1: ",a[0],"2: ",a[1],"\n3: ",a[2], "4: ",a[3],"\n5: ",a[4], "6: ",a[5])
            # print(x_3, y_3, z_3)
            # print(theta_3)
        except:
            pass
        
        

        
        # self.data.points = [self.point]
        # self.publisher.publish(self.data)

        # print(theta_1*180/pi)
        # print(theta_2*180/pi)
        # print(theta_3*180/pi)
        # print(theta_4*180/pi)
        # print(theta_5*180/pi)
        # print(theta_6*180/pi)

        

def main():
    rclpy.init()
    node = FrameListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
