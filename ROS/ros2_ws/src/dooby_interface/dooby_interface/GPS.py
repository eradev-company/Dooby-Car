
import serial
import time
import string
import pynmea2

port="/dev/serial0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)

def read_data():
    data=ser.readline()
    if ( data[0:6].decode("utf-8") == "$GPRMC" ):
        msg=pynmea2.parse(data.decode("utf-8"))
        return msg.latitude, msg.longitude
        