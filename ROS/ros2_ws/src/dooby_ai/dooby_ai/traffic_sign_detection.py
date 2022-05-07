import rclpy
from rclpy.node import Node
from rclpy.qos import QoSReliabilityPolicy
from rclpy.qos import QoSProfile

from std_msgs.msg import String
from sensor_msgs.msg import Image


class CameraSubscriber(Node):

    def __init__(self):
        
        # set qos profile
        qos_profile = QoSProfile(depth=1)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
    
        super().__init__('traffic_sign_detector')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.listener_callback,
            qos_profile)
        self.subscription  # prevent unused variable warning
        
        self.publisher = self.create_publisher(
            Image,
            '/camera/image_annotated',
            10)

    def listener_callback(self, msg):
        self.get_logger().info('Recieved an image.')
        self.publisher.publish(msg)
        
        self.get_logger().info('Published an image.')
        

def main(args=None):
    
    rclpy.init(args=args)
    
    camera_subscriber = CameraSubscriber()
    
    rclpy.spin(camera_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    camera_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
