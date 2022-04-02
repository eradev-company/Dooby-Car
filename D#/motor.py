from this import d
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
   
def forward(delay, speed=duty_cycle):
    r.ChangeDutyCycle(speed)
    l.ChangeDutyCycle(speed)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    sleep(delay)

def backward(delay, speed=duty_cycle):
    r.ChangeDutyCycle(speed)
    l.ChangeDutyCycle(speed)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    sleep(delay)


def left(delay, speed=duty_cycle):
     r.ChangeDutyCycle(speed)
     l.ChangeDutyCycle(speed)
     GPIO.output(in1,GPIO.HIGH)
     GPIO.output(in2,GPIO.LOW)
     GPIO.output(in3,GPIO.LOW)
     GPIO.output(in4,GPIO.HIGH)
     sleep(delay)

def right(delay, speed=duty_cycle):
    r.ChangeDutyCycle(speed)
    l.ChangeDutyCycle(speed)
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

def increase_speed():
    global duty_cycle
    if duty_cycle < 100:
        duty_cycle += 10
        r.ChangeDutyCycle(duty_cycle)
        l.ChangeDutyCycle(duty_cycle)

def decrease_speed():
    global duty_cycle
    if duty_cycle > 10:
        duty_cycle = duty_cycle - 10
        r.ChangeDutyCycle(duty_cycle)
        l.ChangeDutyCycle(duty_cycle)

def cleanup():
    GPIO.cleanup()