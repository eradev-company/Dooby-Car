import rclpy

from mpu6050 import mpu6050 as MPU
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')
        self.publisher_ = self.create_publisher(
            Imu,
            '/imu',
            10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
        try:
            self.MPU = MPU(0x68)
        except:
            pass


    def timer_callback(self):
            # Create a new message
            try:
                acc = self.MPU.get_accel_data()
                gyro = self.MPU.get_gyro_data()

                msg = Imu()
                msg.header.stamp = self.get_clock().now().to_msg()
                msg.header.frame_id = '/base_link'
                msg.linear_acceleration.x = acc['x']
                msg.linear_acceleration.y = acc['y']
                msg.orientation.x = gyro['x']
                msg.orientation.y = gyro['y']

                # Publish the message
                self.publisher_.publish(msg)
                self.get_logger().info('Published imu coordinates.')
            except:
                pass


    
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