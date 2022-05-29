import socketio
import json
import _thread
import time
import rel
import requests
#from Colors import greenOn

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

sio = socketio.Client()

sio.connect('https://dooby-car.herokuapp.com')

print(sio.get_sid())

print('my sid is', sio.sid)


@sio.on('unlock-notif')
def on_message(data):
    print('Unlocking ...')
    greenOn()
    print('Car is open')
    
    
@sio.on('ride-notif')
def on_message(data):
    received = json.loads(data)
    print('going from')
    print('lat = '+ received['from_location_x'] + ', lng = ' + received['from_location_y'])
    print('To')
    print('lat = '+ received['to_location_x'] + ', lng = ' + received['to_location_y'])
    
@sio.on('cancel-ride-notif')
def on_message(data):
    print('Canceling the ride ...')

@sio.event
def connect():
    print("I'm connected!")
    requests.post('https://dooby-car.herokuapp.com/vehicules/updateVehiculeSocket/',
                  data = {'socket_id': sio.get_sid()})
    #update socket_id {config + database}
    #sio.emit('id-message', json.dumps({'type': 'just a test', 'id': sio.get_sid()}))
    

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")
    
    
requests.post('https://dooby-car.herokuapp.com/vehicules/updateVehiculeSocket/',
                  {'socket_id': sio.get_sid(), 'id': 1})

#requests.post('http://doo-by.heroku-app.com/vehicules/updateVehiculeSocket/')
# update socket_id 
# sio.emit('id-message', json.dumps({'type': 'just a test', 'id': sio.get_sid()}))