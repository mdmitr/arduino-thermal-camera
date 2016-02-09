/*
Arduino Servo Test sketch
*/
#include <SoftwareSerial.h>
#include "SerialCommand.h"
#include <Servo.h>
#include <i2cmaster.h>

#define LR_SERVO 9
#define UD_SERVO 10

Servo servo_lr; // Define our Servo
Servo servo_ud;
SerialCommand cmd;

float servo_lr_ms;
float servo_ud_ms;

int servo_delay_per_ms = 4;
int servo_min_delay = 20;
int servo_max_delay = 1000;
int sensor_delay = 50;

void setup()
{
   servo_lr_ms = 1500;
   servo_ud_ms = 1500;
   servo_lr.writeMicroseconds(servo_lr_ms);
   servo_lr.attach(LR_SERVO, 1100, 1700); // servo on digital pin 10
   servo_ud.writeMicroseconds(servo_ud_ms);
   servo_ud.attach(UD_SERVO);

   delay(1000);
   //servo_lr.detach();
   //servo_ud.detach();

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
  
  if (servo_ud.attached())
    servo_ud.detach();
  /*
  if (servo_lr.attached() == false)
    servo_lr.attach(LR_SERVO);
  */
  char * arg = cmd.next();
  float ms = atoi(arg);
  if (ms == servo_lr_ms)
  {
    Serial.println("Ok");
    return;
  }
  
  servo_lr.writeMicroseconds(ms);
  delay(max(servo_min_delay,min(servo_max_delay,abs(ms-servo_lr_ms)*servo_delay_per_ms)));
  //servo_lr.detach();
  servo_lr_ms = ms;
  Serial.println("Ok");
}

void ud()
{
  /*
  if (servo_lr.attached())
    servo_lr.detach();
    */
  if (servo_ud.attached() == false)
    servo_ud.attach(UD_SERVO);
  
  char * arg = cmd.next();
  float ms = atoi(arg);
  if (ms == servo_ud_ms)
  {
    Serial.println("Ok");
    return;
  }
  
  servo_ud.writeMicroseconds(ms);
  delay(max(servo_min_delay,min(servo_max_delay,abs(ms-servo_ud_ms)*servo_delay_per_ms)));
  //servo_ud.detach();
  servo_ud_ms = ms;
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

    delay(sensor_delay);
    
    Serial.println("Ok");
    Serial.println(celcius);
}


