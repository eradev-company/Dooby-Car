import RPi.GPIO as GPIO          
from time import sleep

in1 = 24
in2 = 23
in3= 6
in4 = 5
en1 = 17
en2 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
r=GPIO.PWM(en1,1000)
l=GPIO.PWM(en2,1000)
global duty_cycle
duty_cycle = 100
r.start(duty_cycle)
l.start(duty_cycle)
   
   
def set_speed(linear_speed, angular_speed):
    default_delay = 3
    if linear_speed > 0:
        forward(linear_speed , default_delay)
    elif linear_speed < 0:
        backward(-linear_speed , default_delay)
    elif linear_speed == 0:
        stop()
        if angular_speed > 0:
            right(angular_speed , default_delay)
        elif  angular_speed < 0:
            left(-angular_speed , default_delay)
        
    
    return

def forward(speed, delay=0.5):
    r.ChangeDutyCycle(speed*100)
    l.ChangeDutyCycle(speed*100)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(delay)

def backward(speed, delay=0.5):
    r.ChangeDutyCycle(speed*100)
    l.ChangeDutyCycle(speed*100)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(delay)


def left(speed, delay=0.5):
     r.ChangeDutyCycle(speed*100)
     l.ChangeDutyCycle(speed*100)
     GPIO.output(in1,GPIO.HIGH)
     GPIO.output(in2,GPIO.LOW)
     GPIO.output(in3,GPIO.LOW)
     GPIO.output(in4,GPIO.HIGH)
     sleep(delay)

def right(speed, delay=0.5):
    r.ChangeDutyCycle(speed*100)
    l.ChangeDutyCycle(speed*100)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(delay)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    

def cleanup():
    GPIO.cleanup()