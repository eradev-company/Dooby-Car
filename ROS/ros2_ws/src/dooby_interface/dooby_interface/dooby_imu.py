import rclpy

from dooby_interface import HMC
from rclpy.node import Node
from sensor_msgs.msg import Imu
import math

class ImuPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')
        self.publisher_ = self.create_publisher(
            Imu,
            '/imu',
            10)
        timer_period = 0.2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        initial_angle = HMC.read_data()


    # convert yaw to quaternion
    def quaternion_from_angle(self , yaw):
        # convert yaw from degree to radian
        yaw_rad = yaw * (math.pi / 180)
        q = [0.0, 0.0, 0.0, 0.0]
        q[0] = np.cos(yaw_rad * 0.5)
        q[1] = 0.0
        q[2] = 0.0
        q[3] = 1.0
        return q  
        

    def timer_callback(self):
            # Create a new message
            angle = HMC.read_data()
            delta_angle = angle - initial_angle

            msg = Imu()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.header.frame_id = 'base_link'

            # convert gyro x and y to quaternion
            q = self.quaternion_from_angle(angle)
            msg.orientation.x = q[0]
            msg.orientation.y = q[1]
            msg.orientation.z = q[2]
            msg.orientation.w = q[3]

            # set covariance
            msg.orientation_covariance = [0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.01]

            # Publish the message
            self.publisher_.publish(msg)
            self.get_logger().info('Published imu coordinates.')


    
def main(args=None):
    rclpy.init(args=args)

    imu_publisher = ImuPublisher()
    
    rclpy.spin(imu_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    imu_publisher.destroy_node()
   
    rclpy.shutdown()


if __name__ == '__main__':
    main()