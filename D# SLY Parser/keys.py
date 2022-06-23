import time
import motor
from sshkeyboard import listen_keyboard

def press(key):
        if key=='8':
            motor.forward(delay=0.01)
            print("forward")

        elif key =='2':
            motor.backward(delay=0.01)
            print("backward")

        elif key =='5':
            print("stop")
            motor.stop()

        elif key =='4':
            print("left")
            motor.left(delay=0.01)

        elif key =='6':
            print("right")
            motor.right(delay=0.01)     

        elif key =='9':
            motor.increase_speed()
            print("increase speed to {}".format(motor.duty_cycle))

        elif key =='3':
            motor.decrease_speed()
            print("decrease speed to {}".format(motor.duty_cycle))

        else:
            print("<<<  wrong key  >>>")

def release(key):
    motor.stop()

try:
    listen_keyboard(
    on_press=press,
    on_release=release)

except KeyboardInterrupt:
    print("<<<  KeyboardInterrupt  >>>")
    motor.stop()
    motor.cleanup()
