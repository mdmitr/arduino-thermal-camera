from math import nan
from random import random
import serial
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
import os.path

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

    try:
        arduino = serial.Serial('\\.\COM' + str(Settings.settings['comport']), 9600, timeout=5)
    except serial.SerialException as e:
        if os.path.isfile('.noarduino'):
            arduino = None
        else:
            QMessageBox.critical(None, "Connection to COM3", "Failed to connect to COM3: "+str(e))
            exit()
        pass
    test_temp = 12

    def __init__(self):
        super().__init__()
        self.lrServoMS = self.get_lr_servo()
        self.udServoMS = self.get_ud_servo()
        return

    def execute_command(self, command, *params):
        if len(params) is 0:
            arduino_command = "{0}\r\n".format(command)
        else:
            arduino_command = "{0} {1}\r\n".format(command, *params)
        if self.arduino is not None:
            self.arduino.write(str.encode(arduino_command))
        else:
            print(str.encode(arduino_command)[:-2])

    def read_float(self):
        if self.arduino is not None:
            value = self.arduino.readline()
            if len(value) > 0:
                return float(value.decode()[:-2])
        return nan

    def read_int(self):
        if self.arduino is not None:
            value = self.arduino.readline()
            if len(value) > 0:
                return int(value.decode()[:-2])
        return nan

    def set_lr_servo(self, ms):
        self.lrServoMS = ms
        self.execute_command(Command.lr, ms)
        self.lr_servo_changed.emit(self.lrServoMS)

    def get_lr_servo(self):
        self.execute_command(Command.rlr)
        self.lrServoMS = self.read_int()

    def set_ud_servo(self, ms):
        self.udServoMS = ms
        self.execute_command(Command.ud, ms)
        self.ud_servo_changed.emit(self.udServoMS)

    def get_ud_servo(self):
        self.execute_command(Command.rud)
        self.lrServoMS = self.read_int()

    def temperature(self):
        self.execute_command(Command.t)
        return 30+random()*50 #  self.read_float()


arduinoCtrl = ArduinoCtrl()


