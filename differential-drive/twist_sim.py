from dooby_motorDriver import MotorDriver



class RobotMover(object):

    def __init__(self):
        self.motor_driver = MotorDriver()


    def cmd_vel_callback(self):
        linear_speed = 20
        angular_speed = 0
        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        linear_speed = 10
        angular_speed = 170
        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        linear_speed = 20
        angular_speed = 0
        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        for i in range(14) :
            linear_speed = 10
            angular_speed = -165
            # Decide Speed
            self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        linear_speed = 20
        angular_speed = 0
        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        linear_speed = 10
        angular_speed = 300
        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        linear_speed = 20
        angular_speed = 0
        # Decide Speed
        self.motor_driver.set_cmd_vel(linear_speed, angular_speed)
        

        # linear_speed = 5
        # angular_speed = -175
        # # Decide Speed
        # self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

        # linear_speed = 5
        # angular_speed = -175
        # # Decide Speed
        # self.motor_driver.set_cmd_vel(linear_speed, angular_speed)

    def cmd_vel_callback2(self, linear_s, angular_s) :
        self.motor_driver.set_cmd_vel(linear_s, angular_s)


robot_mover = RobotMover()

def moveDoobyCar(linearspeed, angularspeed) :
    robot_mover.cmd_vel_callback2(linearspeed, angularspeed)

    

    