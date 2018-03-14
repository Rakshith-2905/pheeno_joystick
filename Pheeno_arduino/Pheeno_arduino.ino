 #include "PheenoV2Basic.h"

// Instantiate Pheeno class
PheenoV2Basic my_robot = PheenoV2Basic(1);

#define pi 3.14


//Motor vaiables
float linear_vel = 0; // in cm/sec
float angular_vel = 0; //in rad/sec
float linear_velocity = 0; // in cm/sec
float angular_velocity = 0; //in rad/sec


void setup() {

  Serial.begin(9600);
  my_robot.SetupBasic();

}

void loop() {

      SerialEvent();

  }

// Reads serial communication information, if present.
void SerialEvent() {
  while (Serial.available()) {

    char in_char = (char)Serial.read();  // Get the new byte.
    in_data += in_char;                  // Add it to the input string.

    // If the incoming character is a : it denotes end of message
    if (in_char == ';') {
      //Serial.println("in_data");
      ParseData();
      in_data = "";
      }
    }
    // Move robot forward. Pheeno moves forward at a given speend (range 0-255) and angle as degrees
    Pheeno_Move(0,0);
  }

void ParseData()
{

  if(in_data!=""){

    if (in_data.indexOf(';') >= 0)
    {
      linear_vel = in_data.substring(0, in_data.indexOf(":"));
      angular_vel = in_data.substring((in_data.indexOf(":")+1), in_data.indexOf(";"));

      linear_vel = linear_vel.toInt();
      angular_vel = angular_vel.toInt();

      linear_velocity = map(linear_vel,-255,255,-20,20)
      angular_velocity = map(angular_vel,-255,255,-1.57,1.57)
      // Move robot forward. Pheeno moves forward at a given speend (range 0-255) and angle as degrees
      Pheeno_Move(Linear_vel,angle);
    }
    Pheeno_Move(0,0);
  }
