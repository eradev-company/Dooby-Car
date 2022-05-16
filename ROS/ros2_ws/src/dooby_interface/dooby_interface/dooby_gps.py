import rclpy
from dooby_interface import GPS

from rclpy.node import Node
from sensor_msgs.msg import NavSatFix


class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(
            NavSatFix,
            'gps',
            10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0


    def timer_callback(self):
        # Create a new message
        x, y = GPS.getPositionData()
        msg = NavSatFix()
        msg.header.stamp = self.get_clock.to_msg()
        msg.header.frame_id = 'gps'
        msg.latitude = x
        msg.longitude = y
        msg.altitude = 0
        
        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info('Published gps coordinates.')
        
        
    
def main(args=None):
    rclpy.init(args=args)

    gps_publisher = GPSPublisher()
    
    rclpy.spin(gps_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gps_publisher.destroy_node()
   
    rclpy.shutdown()


if __name__ == '__main__':
    main()