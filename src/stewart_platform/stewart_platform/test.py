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
        a=DynamicJointState()
        a.interface_values
        b=Float64MultiArray()
        self.publisher = self.create_publisher(Float64MultiArray, 'joint_effort_controller/commands', 10)
        
        self.aa=Float64MultiArray()
        self.error_1=0
        self.i_1=0
        self.target=-1.0
    def callback(self, msg):
        self.error_old_1=self.error_1

        self.error_1=self.target-msg.interface_values[0].values[0]

        kp=5
        kd=0.1
        ki=1

        self.i_1+=self.error_1
        d_1=(self.error_1-self.error_old_1)
        revolute1=self.error_1*kp+self.i_1*ki+d_1*kd

        self.aa.data=[revolute1]
   
        self.publisher.publish(self.aa)




def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
