import rclpy
from rclpy.node import Node
from math import pi

from control_msgs.msg import DynamicJointState, InterfaceValue
from std_msgs.msg import Float64MultiArray

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            DynamicJointState,
            'dynamic_joint_states',
            self.callback,
            10)
        self.subscription = self.create_subscription(
            Float64MultiArray,
            'ik_solution',
            self.ik_callback,
            10)
        self.publisher = self.create_publisher(Float64MultiArray, 'joint_effort_controller/commands', 10)
        
        self.aa=Float64MultiArray()
        self.error_1=0
        self.error_2=0
        self.error_3=0
        self.error_4=0
        self.error_5=0
        self.error_6=0
  
        self.i_1=0
        self.i_2=0
        self.i_3=0
        self.i_4=0
        self.i_5=0
        self.i_6=0

        self.target_1=0
        self.target_2=0
        self.target_3=0
        self.target_4=0
        self.target_5=0
        self.target_6=0


    def ik_callback(self,msg):
        self.target_1=msg.data[0]
        self.target_2=msg.data[1]
        self.target_3=msg.data[2]
        self.target_4=msg.data[3]
        self.target_5=msg.data[4]
        self.target_6=msg.data[5]

    def callback(self, msg):

        self.error_old_1=self.error_1
        self.error_old_2=self.error_2
        self.error_old_3=self.error_3
        self.error_old_4=self.error_4
        self.error_old_5=self.error_5
        self.error_old_6=self.error_6

        self.error_2=self.target_2-msg.interface_values[4].values[0]
        self.error_4=self.target_4-msg.interface_values[1].values[0]
        self.error_6=self.target_6-msg.interface_values[5].values[0]
        
        self.error_1=self.target_1-msg.interface_values[3].values[0]
        self.error_3=self.target_3-msg.interface_values[0].values[0]
        self.error_5=self.target_5-msg.interface_values[2].values[0]
        
        kp=10
        kd=10
        ki=0.1

        self.i_1+=self.error_1
        d_1=(self.error_1-self.error_old_1)
        revolute1=self.error_1*kp+self.i_1*ki+d_1*kd

        self.i_2+=self.error_2
        d_2=(self.error_2-self.error_old_2)
        revolute2=self.error_2*kp+self.i_2*ki+d_2*kd

        self.i_3+=self.error_3
        d_3=(self.error_3-self.error_old_3)
        revolute3=self.error_3*kp+self.i_3*ki+d_3*kd

        self.i_4+=self.error_4
        d_4=(self.error_4-self.error_old_4)
        revolute4=self.error_4*kp+self.i_4*ki+d_4*kd

        self.i_5+=self.error_5
        d_5=(self.error_5-self.error_old_5)
        revolute5=self.error_5*kp+self.i_5*ki+d_5*kd

        
        self.i_6+=self.error_6
        d_6=(self.error_6-self.error_old_6)
        revolute6=self.error_6*kp+self.i_6*ki+d_6*kd
     
        self.aa.data=[revolute1, revolute2,revolute3,revolute4, revolute5, revolute6]
   
        self.publisher.publish(self.aa)

    


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
