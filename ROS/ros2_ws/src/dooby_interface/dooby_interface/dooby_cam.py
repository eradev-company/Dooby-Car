import rclpy

from cv_bridge import CvBridge

import cv2
from rclpy.node import Node
from sensor_msgs.msg import Image

class CamPublisher(Node):

    def __init__(self):
        super().__init__('cam_publisher')
        self.publisher_ = self.create_publisher(
            Image,
            '/camera/image_raw',
            10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)
        self.bridge = CvBridge()


    def get_image(self):
            ret, frame = self.cap.read()
            if ret:
                return frame
            else:
                return None


    def timer_callback(self):
        frame = self.get_image()
        #reshape the frame to be a numpy array
        frame = cv2.resize(frame, (128, 96))
        # use cvbridge to convert the frame to a ROS message
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "camera"
        self.publisher_.publish(msg)
        self.get_logger().info('Published image.')



    
def main(args=None):
    rclpy.init(args=args)

    cam_publisher = CamPublisher()
    
    rclpy.spin(cam_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cam_publisher.destroy_node()
   
    rclpy.shutdown()


if __name__ == '__main__':
    main()