from random import random
import serial
from PyQt5.QtCore import QObject, pyqtSignal

import Settings

class Command:
    lr = 'lr'   # calls left-right servo writeMicroseconds
    ud = 'ud'   # calls up-down servo writeMicroseconds
    rlr = 'rlr'
    rud = 'rud'
    s = 's'    # calls for both servos setMicroSeconds, or getMicroseconds if parameter is ?
    t = 't'    # get temperature at current point

class ArduinoCtrl(QObject):

    lr_servo_changed = pyqtSignal(int)
    ud_servo_changed = pyqtSignal(int)
    arduino = serial.Serial('\\.\COM' + str(Settings.settings['comport']), 9600, timeout=5)
    test_temp = 12

    def __init__(self):
        super().__init__()
        #self.lrServoMS = self.execute_command(Command.rlr, Settings.settings['lrServoCenter'])[0]
        self.lrServoMS = int(self.execute_command(Command.rlr))
        self.udServoMS = int(self.execute_command(Command.rud))
        return

    def execute_command(self, command, *params):
        if len(params) is 0:
            arduino_command = "{0}\r\n".format(command)
        else:
            arduino_command = "{0} {1}\r\n".format(command, *params)
        self.arduino.write(str.encode(arduino_command))
        value = self.arduino.readline()
        if len(value) > 0:
            return float(value.decode()[:-2])
        return -1

    def set_lr_servo(self, ms):
        self.lrServoMS = int(self.execute_command(Command.lr, ms))
        self.lr_servo_changed.emit(self.lrServoMS)

    def set_ud_servo(self, ms):
        self.udServoMS = int(self.execute_command(Command.ud, ms)[0])
        self.ud_servo_changed.emit(self.udServoMS)

    def temperature(self, lr_ms, ud_ms):
        self.execute_command(Command.t, lr_ms, ud_ms)
        return 30+random()*50




arduinoCtrl = ArduinoCtrl()


