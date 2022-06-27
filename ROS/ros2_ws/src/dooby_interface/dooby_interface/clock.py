import rclpy

from rclpy.node import Node

#Clock message
from rosgraph_msgs.msg import Clock

import math

class ClockPublisher(Node):
    
        def __init__(self):
            super().__init__('clock_publisher')
            self.publisher_ = self.create_publisher(
                Clock,
                '/clock',
                10)
    
            timer_period = 0.1  # seconds
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.i = 0.0
    
        def timer_callback(self):
    
            # Create a new message
            msg = Clock()
            # floor of i
            msg.clock.sec = math.floor(self.i)
            msg.clock.nanosec = int((self.i - math.floor(self.i)) * 1000000000)

    
            # Publish the message
            self.publisher_.publish(msg)
            self.get_logger().info('Published clock.')
            self.i += 0.1


def main(args=None):
    rclpy.init(args=args)

    clock_publisher = ClockPublisher()

    rclpy.spin(clock_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    clock_publisher.destroy_node()

if __name__ == '__main__':
    main()
