from gps import *
import json

def gpsInfo():
    nx = gpsd.next()
    if nx['class'] == 'TPV':
        latitude = getattr(nx, 'lat', "Unknown")
        longitude = getattr(nx, 'lon', "Unknown")
        print ("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
        return json.dumps({'lon': str(longitude), 'lat': str(latitude)})
        