import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from ackermann_msgs.msg import AckermannDrive


class AppCom(Node):
    def __init__(self):
        super().__init__('app_com')
        self.publisher_steering_ = self.create_publisher(AckermannDrive, '/pilsbot_velocity_controller/cmd_vel', 2)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = AckermannDrive()
        msg.steering_angle = -0.2
        msg.steering_angle_velocity = 0.1
        msg.speed = 0.14
        #msg.acceleration = 0.001
        #msg.jerk = 0.001
        self.publisher_steering_.publish(msg)
        print(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    app_com = AppCom()
    rclpy.spin(app_com)
    app_com.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
