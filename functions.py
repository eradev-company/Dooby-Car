import requests
import json
import threading
import time
import config
# from GPS import gpsInfo

try:
    with open('config.json') as f:
        config = json.load(f)
        f.close()
except FileNotFoundError:
    try:
        import config
    except Exception as e:
        raise SomeMoreAopropriateError()
    with open('config.json', 'w') as f:
        json.dump(config, f)
        f.close()

        
def OnDepart():
    with open('config.json') as f:
        config = json.load(f)
        f.close()
    print("I have arrived to depart point")
    print(requests.post('http://dooby-car.herokuapp.com/reservation/vehiculeEnDepart', 
                  {'id': config['reservation_id']}))
    
def OnDest():
    with open('config.json') as f:
        config = json.load(f)
        f.close()
    print("I have arrived to destination point")
    print(requests.post('http://dooby-car.herokuapp.com/reservation/finTrajetDooby', 
                  {'idReservation': config['reservation_id']}))
    
def blockState():
    with open('config.json') as f:
        config = json.load(f)
        f.close()
    print("I can't move forward")
    print(requests.post('http://dooby-car.herokuapp.com/maintenance/addTacheBlocage', 
                  {'idVehicule': config['car_id']}))
        
def getBattery():
    with open('config.json') as f:
        config = json.load(f)
        f.close()
    return config['battery']
       
def getSpeed():
    with open('config.json') as f:
        config = json.load(f)
        f.close()
    return config['speed']

def getTemp():
    with open('config.json') as f:
        config = json.load(f)
        f.close()
    return config['temperature']
    
def getLocation():
    # return gpsInfo()
    return {'lat': 3.25687437, 'lon': 35.69876543}

def checkTemp(temp):
    config['temperature'] = temp + 2
    
    with open('config.json', 'w') as f:
            json.dump(config, f)
            f.close()
            
    if temp > config['max_temp']:
        print("Temperature is too high")
        
        requests.post('http://dooby-car.herokuapp.com/vehicules/updateVehiculeInfoTech', 
                  {'id': config['car_id'], 'battery': getBattery(), 'vitesse': 0, 'temperature': getTemp()})
        # panne
        # print(requests.post('http://dooby-car.herokuapp.com/maintenance/addTacheMaintenance', 
        #           {'idVehicule': config['car_id'], 'type': 'temperature'}))
        # /maintenance/addTachePanne
        
        #sleep until temperature is under max_temp
        while temp > config['max_temp']:
            temp = getTemp() 
            time.sleep(2)
            # light is on (loop: red light on then off)
        
    elif temp < config['min_temp']:
        print("Temperature is too low")
        
        requests.post('http://dooby-car.herokuapp.com/vehicules/updateVehiculeInfoTech', 
                  {'id': config['car_id'], 'battery': getBattery(), 'vitesse': 0, 'temperature': getTemp()})
        # panne
        # print(requests.post('http://dooby-car.herokuapp.com/maintenance/addTacheMaintenance', 
        #           {'idVehicule': config['car_id'], 'type': 'temperature'}))
        
        #sleep until temperature is above min_temp
        while temp < config['min_temp']:
            temp = getTemp()
            time.sleep(2)
            # light is on (loop: red light on then off)
            
    else:
        print("Temperature is ok")

def update_info():
    battery = getBattery()
    vitesse = getSpeed()
    temperature = getTemp()
    checkTemp(temperature)
    requests.post('http://dooby-car.herokuapp.com/vehicules/updateVehiculeInfoTech', 
                  {'id': config['car_id'], 'battery': battery, 'vitesse': vitesse, 'temperature': temperature})

    