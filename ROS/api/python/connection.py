import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

print('Connected to ROS2 !')
client.terminate()