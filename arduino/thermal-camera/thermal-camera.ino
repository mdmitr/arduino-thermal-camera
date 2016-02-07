/*
Arduino Servo Test sketch
*/
#include <SoftwareSerial.h>
#include "SerialCommand.h"
#include <Servo.h>
#include <i2cmaster.h>


Servo servo_lr; // Define our Servo
Servo servo_ud;
SerialCommand cmd;

void setup()
{
   servo_lr.attach(10, 1100, 1700); // servo on digital pin 10
   servo_ud.attach(11, 550, 900);

   i2c_init(); //Initialise the i2c bus
   PORTC = (1 << PORTC4) | (1 << PORTC5);//enable pullups

   
   Serial.begin(9600);

   cmd.addCommand("lr", lr);
   cmd.addCommand("ud", ud);
   cmd.addCommand("rlr", rlr);
   cmd.addCommand("rud", rud);
   cmd.addCommand("t", t);
}

void loop()
{
  cmd.readSerial();
}

void lr()
{
  float prev_ms = servo_lr.readMicroseconds();
  char * arg = cmd.next();
  float ms = atoi(arg);
  servo_lr.writeMicroseconds(ms);
  delay(abs(ms-prev_ms)*1);
  Serial.println("Ok");
}

void ud()
{
  float prev_ms = servo_lr.readMicroseconds();
  char * arg = cmd.next();
  float ms = atoi(arg);
  servo_ud.writeMicroseconds(ms);
  delay(min(100,abs(ms-prev_ms)*5));
  Serial.println("Ok");
}

void rlr()
{
  Serial.println("Ok");
  Serial.println(servo_lr.readMicroseconds());
}

void rud()
{
  Serial.println("Ok");
  Serial.println(servo_ud.readMicroseconds());
}

void t()
{
    int dev = 0x5A<<1;
    int data_low = 0;
    int data_high = 0;
    int pec = 0;
    
    i2c_start_wait(dev+I2C_WRITE);
    i2c_write(0x07);
    
    // read
    i2c_rep_start(dev+I2C_READ);
    data_low = i2c_readAck(); //Read 1 byte and then send ack
    data_high = i2c_readAck(); //Read 1 byte and then send ack
    pec = i2c_readNak();
    i2c_stop();
    
    //This converts high and low bytes together and processes temperature, MSB is a error bit and is ignored for temps
    double tempFactor = 0.02; // 0.02 degrees per LSB (measurement resolution of the MLX90614)
    double tempData = 0x0000; // zero out the data
    int frac; // data past the decimal point
    
    // This masks off the error bit of the high byte, then moves it left 8 bits and adds the low byte.
    tempData = (double)(((data_high & 0x007F) << 8) + data_low);
    tempData = (tempData * tempFactor)-0.01;
    
    float celcius = tempData - 273.15;
    Serial.println("Ok");
    //delay(20);
    Serial.println(celcius);
}


