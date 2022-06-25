import RPi.GPIO as GPIO
import time
   
GPIO.setmode(GPIO.BCM)
   
# The output pins will be declared, which are connected with the LEDs.
LED_RED = 20
LED_GREEN = 21
GPIO.setup(LED_RED, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED_GREEN, GPIO.OUT, initial= GPIO.LOW)
        
def greenOn():
    try:
        GPIO.output(LED_RED,GPIO.LOW) #LED off
        GPIO.output(LED_GREEN,GPIO.HIGH) #LED on
    except KeyboardInterrupt:
        GPIO.cleanup()
        
def redOn():
    try:
        GPIO.output(LED_GREEN,GPIO.LOW) #LED off
        GPIO.output(LED_RED,GPIO.HIGH) #LED on
    except KeyboardInterrupt:
        GPIO.cleanup()
        
def turnOFF():
    try:
        GPIO.output(LED_GREEN,GPIO.LOW) #LED off
        GPIO.output(LED_RED,GPIO.LOw) #LED on
    except KeyboardInterrupt:
        GPIO.cleanup()