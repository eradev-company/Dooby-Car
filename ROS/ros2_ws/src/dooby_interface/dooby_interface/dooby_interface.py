import rclpy
#from dooby_interface import motor

from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from geometry_msgs.msg import TwistWithCovariance
from geometry_msgs.msg import PoseWithCovariance
from geometry_msgs.msg import TransformStamped

from dooby_interface import motor
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
import math
import tf2_ros


class Interface(Node):
    
    def __init__(self):
        super().__init__('dooby_interface')

        # initialize global variables
        # position variables
        self.x = 0.0
        self.y = 0.0

        # orientation variable
        self.theta = 0.0

        # velocities 
        self.vx = 0.0

        # angular velocity
        self.vz = 0.0

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        timer_period = 0.2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.publisher = self.create_publisher(
            Odometry,
            '/odom',
            10)

        motor.set_speed(0.0, 0.0)

        # current time set to now
        self.t = self.get_clock().now()
        self.odom_msg = Odometry()
        self.odom_msg.header.stamp = self.t.to_msg()
        self.odom_msg.header.frame_id = 'odom'
        self.odom_msg.child_frame_id = 'base_link'


    def timer_callback(self):
        # calculate new position
        new_t = self.get_clock().now()
        self.x = self.x + 2.0 * self.vx * math.cos(self.theta) * (new_t - self.t).nanoseconds / 1e9
        self.y = self.y + 2.0 * self.vx * math.sin(self.theta) * (new_t - self.t).nanoseconds / 1e9
        self.theta = self.theta + 4.0 * self.vz * (new_t - self.t).nanoseconds / 1e9
        self.t = new_t

        # prepare odometry message
        self.odom_msg.header.stamp = self.t.to_msg()
        self.odom_msg.header.frame_id = 'odom'
        self.odom_msg.child_frame_id = 'base_link'
        self.odom_msg.pose.pose.position.x = self.x
        self.odom_msg.pose.pose.position.y = self.y
        self.odom_msg.pose.pose.orientation.z = math.sin(self.theta / 2)
        self.odom_msg.pose.pose.orientation.w = math.cos(self.theta / 2)
        self.odom_msg.twist.twist.linear.x = self.vx
        self.odom_msg.twist.twist.angular.z = self.vz

        # set covariance
        self.odom_msg.pose.covariance = [0.1, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.1, 0.0, 0.0, 0.0, 0.0,
                                        0.0 , 0.0, 0.1, 0.0, 0.0, 0.0,
                                        0.0 , 0.0, 0.0, 0.1, 0.0, 0.0,
                                        0.0 , 0.0, 0.0, 0.0, 0.1, 0.0,
                                        0.0 , 0.0, 0.0, 0.0, 0.0, 0.1]
        
        self.odom_msg.twist.covariance = [0.1, 0.0, 0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.1, 0.0, 0.0, 0.0, 0.0,
                                        0.0 , 0.0, 0.1, 0.0, 0.0, 0.0,
                                        0.0 , 0.0, 0.0, 0.1, 0.0, 0.0,
                                        0.0 , 0.0, 0.0, 0.0, 0.1, 0.0,
                                        0.0 , 0.0, 0.0, 0.0, 0.0, 0.1]


        self.publisher.publish(self.odom_msg)
        self.get_logger().info('Published odometry')

    def listener_callback(self, msg):
        self.get_logger().info('Recieved a twist command.')
        
        # update global variables
        if msg.angular.z > 0.3 :
            self.vx = 0.0
            self.vz = 0.6
        elif msg.angular.z < - 0.3 :
            self.vx = 0.0
            self.vz = -0.6
        else:
            self.vx = msg.linear.x
            self.vz = 0.0

        try:
            motor.set_speed(self.vz, self.vx)
        finally:
            pass
            
def main(args=None):
    rclpy.init(args=args)

    interface = Interface()
    
    rclpy.spin(interface)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    interface.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()