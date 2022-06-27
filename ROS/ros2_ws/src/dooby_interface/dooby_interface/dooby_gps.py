import rclpy
from dooby_interface import GPS

from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

map_center = [36.705624,3.170748]


class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(
            PoseStamped,
            'gps',
            10)
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0


    def timer_callback(self):
        # Create a new message
        lat, long = GPS.getPositionData()
        msg = PoseStamped()
        msg.header.stamp = self.get_clock.to_msg()
        msg.header.frame_id = 'gps'
        # convert lat and long to x and y
        x = (lat - map_center[0]) * 100000
        y = (long - map_center[1]) * 100000
        
        # set covariance
        msg.pose.covariance = [0.5, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.5]

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