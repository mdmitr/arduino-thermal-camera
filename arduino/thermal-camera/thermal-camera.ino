/*
Arduino Servo Test sketch
*/
#include <SoftwareSerial.h>
#include "SerialCommand.h"
#include <Servo.h>


Servo servo_lr; // Define our Servo
Servo servo_ud;
SerialCommand cmd;

void setup()
{
   servo_lr.attach(10); // servo on digital pin 10
   servo_ud.attach(11);
   Serial.begin(9600);

   cmd.addCommand("lr", lr);
   cmd.addCommand("ud", ud);
   cmd.addCommand("rlr", rlr);
   cmd.addCommand("rud", rud);
}

void loop()
{
  cmd.readSerial();
}

void lr()
{
  char * arg = cmd.next();
  float ms = atoi(arg);
  servo_lr.writeMicroseconds(ms);
}

void ud()
{
  char * arg = cmd.next();
  float ms = atoi(arg);
  servo_ud.writeMicroseconds(ms);
}

void rlr()
{
  Serial.println(servo_lr.readMicroseconds());
}

void rud()
{
  Serial.println(servo_ud.readMicroseconds());
}
