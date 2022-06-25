import requests
import json
import threading
import time
# from GPS import gpsInfo

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

        
def OnDepart():
    print("I have arrived to depart point")
    print(requests.post('http://dooby-car.herokuapp.com/reservation/vehiculeEnDepart', 
                  {'id': config['reservation_id']}))
    

def OnDest():
    print("I have arrived to destination point")
    print(requests.post('http://dooby-car.herokuapp.com/reservation/finTrajetDooby', 
                  {'idReservation': config['reservation_id']}))
    
def blockState():
    print("I can't move forward")
    print(requests.post('http://dooby-car.herokuapp.com/maintenance/addTacheBlocage', 
                  {'idVehicule': config['car_id']}))

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
        
def getBattery(config):
    return config['battery']
    
    
def getSpeed(config):
    return config['speed']

def getTemp(config):
    return config['temperature']
    
def getLocation():
    # return gpsInfo()
    return {'lat': 3.25687437, 'lon': 35.69876543}

def update_info():
    with open('config.json') as f:
        config = json.load(f)
    battery = getBattery(config)
    vitesse = getSpeed(config)
    temperature = getTemp(config)
    latitude = getLocation()['lat']
    longitude = getLocation()['lon']
    requests.post('http://dooby-car.herokuapp.com/vehicules/updateVehiculeInfoTech', 
                  {'id': config['car_id'], 'battery': battery, 'vitesse': vitesse, 'temperature': temperature, 'longitude': longitude, 'latitude':latitude})

    