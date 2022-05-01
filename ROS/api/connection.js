const ROSLIB = require('roslib');


  var ros = new ROSLIB.Ros();

  // If there is an error on the backend, an 'error' emit will be emitted.
  ros.on('error', function(error) {
    console.log(error);
    console.log('Error connecting to websocket server.');
  });

  // Find out exactly when we made a connection.
  ros.on('connection', function() {
    console.log('Connection made!');
  });

  ros.on('close', function() {
    console.log('Connection closed.');
  });

  // Create a connection to the rosbridge WebSocket server.
  ros.connect('ws://husarnet:9090/');
  

  // send twist message
  function sendTwist() {
    linear_x = 0 // api request
    angular_z = 0  // api request
    
    var twist = new ROSLIB.Message({
      linear: {
        x: linear_x,
        y: 0,
        z: 0
      },
      angular: {
        x: 0,
        y: 0,
        z: angular_z
      }
    });
    var twist_pub = new ROSLIB.Topic({
      ros: ros,
      name: '/cmd_vel',
      messageType: 'geometry_msgs/Twist'
    });
    twist_pub.publish(twist);
    console.log('Twist published.');
  }