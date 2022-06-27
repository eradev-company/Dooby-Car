import rclpy

from rclpy.node import Node
from dooby_interface import ultrasonic

#publish laserscan message
from sensor_msgs.msg import LaserScan

class ScanPublisher(Node):

    def __init__(self):
        super().__init__('sonar_publisher')
        self.publisher_ = self.create_publisher(
            LaserScan,
            '/scan',
            10)

        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def  timer_callback(self):

        # read laser scan

        
        # Create a new message
        msg = LaserScan()
        range = ultrasonic.distance()
        # if range > 2.0 set range to + inf
        if range > 2.0:
            range = float('inf')
            
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'
        
        # angles 
        msg.angle_min = -0.1
        msg.angle_max = 0.1
        msg.angle_increment = 0.01
        msg.time_increment = 0.0
        msg.scan_time = 0.0
        msg.range_min = 0.0
        msg.range_max = 3.0
        # set ranges
        msg.ranges = [range/100] * 10
        msg.intensities = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info('Published scan.')
        
        
#main
def main(args=None):
        rclpy.init(args=args)
        
        scan_publisher = ScanPublisher()
        
        rclpy.spin(scan_publisher)
        
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        scan_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()