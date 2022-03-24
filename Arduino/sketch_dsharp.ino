#include <string.h>
#include <SPI.h>
#include <SD.h>

#include <AFMotor.h>
AF_DCMotor left_back_motor(1);
AF_DCMotor right_back_motor(2, MOTOR12_8KHZ);
AF_DCMotor right_front_motor(3);
AF_DCMotor left_front_motor(4);

String line = String("");

#define CS_PIN 26

File root;


enum Command { Forward, Backward, Right, Left, During,  Stop };
 
void setup() {
    Serial.begin(115200);
    delay(2000);
 
    Serial.println(".. Initialized ..");

    Serial.print("Initializing SD card... ");
  
    if (!SD.begin(CS_PIN)) {
      Serial.println("Card initialization failed!");
      while (true);
    }
  
    Serial.println("initialization done.");
  
    Serial.println("Files in the card:");
    root = SD.open("/");
    //printDirectory(root, 0);
    Serial.println("");

    root = SD.open("TEST.TXT");
    if(root){
      Serial.println("File ready ...");
    }
    
}
 
void loop() {
    if(root.available()){
        
        // Read char
        char c = root.read() ;
        Serial.print("First read : ");
        Serial.println(c);
    
        // Construct current line string
        if( c != ' ' && c != '\n' ) {
          //Serial.print("C : ");
          //Serial.println(c);
          line = String(line) + String(c);
        }
        else {

          if( c == ' ' ) {
            
            Serial.println("Finished");
            Serial.print("You typed : ");
            Serial.println(line);


            if( line == "Forward" ) {
                // statements
                Serial.println("Forward");
                int arg = getArgument();
                Serial.println(arg);
                moveForward(arg);
            }
            else if( line == "Backward" ) {
                // statements
                Serial.println("Backward");
                int arg = getArgument();
                Serial.println(arg);
                moveBackward(arg);
            }
            else if( line == "Right" ) {
                // statements
                Serial.println("Right");
                turnRight(getArgument());
            }
            else if( line == "Left" ) {
                // statements
                Serial.println("Left");
                turnLeft(getArgument());
            }
            else if( line == "During" ) {
                // statements
                Serial.println("During");
                int arg = getArgument();
                Serial.println(arg);
                delay(arg);
            }
            else if( line == "Stop" ) {
                // statements
                Serial.println("Stop");
                reset();
            }
            else Serial.println("Unrecognized command");
  
            
          }
          line = String("");
          
        }
    }
}


int getArgument() {
  String arg = "";
  char a = root.read();
  while(root.available() && a != '\n'){

    arg = String(arg) + String(a);
    a = root.read() ;
    
  }
  return arg.toInt();
}

void reset() {
  Serial.println("Resetting");
  
  left_back_motor.setSpeed(0);
  right_back_motor.setSpeed(0);
  right_front_motor.setSpeed(0);
  left_front_motor.setSpeed(0);
}

void moveForward(int speed) {
  Serial.println("Moving forward");
  
  left_back_motor.setSpeed(speed);
  right_back_motor.setSpeed(speed);
  right_front_motor.setSpeed(speed);
  left_front_motor.setSpeed(speed);

  left_back_motor.run (FORWARD);
  right_back_motor.run (FORWARD);
  right_front_motor.run (FORWARD);
  left_front_motor.run (FORWARD);
}

void moveBackward(int speed) {
  Serial.println("Moving backward");
  
  left_back_motor.setSpeed(speed);
  right_back_motor.setSpeed(speed);
  right_front_motor.setSpeed(speed);
  left_front_motor.setSpeed(speed);
  
  left_back_motor.run (BACKWARD);
  right_back_motor.run (BACKWARD);
  right_front_motor.run (BACKWARD);
  left_front_motor.run (BACKWARD);
}

void turnRight(int speed) {
  Serial.println("Turning right");
  
  left_back_motor.setSpeed(speed);
  right_back_motor.setSpeed(0);
  right_front_motor.setSpeed(0);
  left_front_motor.setSpeed(speed);
  
  left_back_motor.run (FORWARD);
  //right_back_motor.run (FORWARD);
  //right_front_motor.run (FORWARD);
  left_front_motor.run (FORWARD);
}

void turnLeft(int speed) {
  Serial.println("Turning left");
  
  left_back_motor.setSpeed(speed);
  right_back_motor.setSpeed(speed);
  right_front_motor.setSpeed(speed);
  left_front_motor.setSpeed(speed);
  
  left_back_motor.run (BACKWARD);
  right_back_motor.run (FORWARD);
  right_front_motor.run (FORWARD);
  left_front_motor.run (BACKWARD);
}
