import requests
import json
import threading
from GPS import gpsInfo

try:
    with open('config.json') as f:
        config = json.load(f)
except FileNotFoundError:
    try:
        import config
    except Exception as e:
        raise SomeMoreAopropriateError()
    with open('config.json', 'w') as f:
        json.dump(config, f)

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
        
def getBattery():
    config.battery = 5
    
    
def getSpeed():
    config.speed = 5
    
def getLocation():
    return gpsInfo()

def update_info():
    battery = getBattery()
    vitesse = getSpeed()
    latitude = getLocation['lat']
    longitude = getLocation['lon']
    #requests.post('http://doo-by.heroku-app.com/vehicules/updateVehicule/')

if __name__ == "__main__":
    setInterval(update_info, 2)
    