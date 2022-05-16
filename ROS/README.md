# ROS Workspace


### install docker on rasp  
please refer to [https://dev.to/elalemanyo/how-to-install-docker-and-docker-compose-on-raspberry-pi-1mo](this blog)
## How to run
  
first, delete old vpn adresses on https://app.husarnet.com/  
creds : gm_sahraoui@esi.dz / dooby1234 
### start developement node :
```
cd Dooby-car/ROS/dev-node
docker-compose up --build
```
Vnc server will be listening on port 6080  
open a terminal in the desktop environment and run:  
```
cd /app/ros2_ws
. install/setup.sh
ros2 launch dooby_simulation display.launch.py
```

### raspberry pi node : 
```
cd Dooby-car/ROS/pi-node
docker-compose up --build
```
the rasp node runs dooby interface packages  
for developing restart docker-compose stack to rebuild

### server node :
```
cd Dooby-car/ROS/server-node
docker-compose up --build
```
the server node runs "navigation2" stack   