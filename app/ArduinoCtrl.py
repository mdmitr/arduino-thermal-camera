from random import random

from PyQt5.QtCore import QObject, pyqtSignal

class Command:
    lr = 'lr'   # calls left-right servo setMicroSeconds, or getMicroseconds if parameter is ?
    ud = 'ud'   # calls up-down servo setMicroSeconds, or getMicroseconds if parameter is ?
    s = 's'    # calls for both servos setMicroSeconds, or getMicroseconds if parameter is ?
    t = 't'    # get temperature at current point

class ArduinoCtrl(QObject):

    lr_servo_changed = pyqtSignal(int)
    ud_servo_changed = pyqtSignal(int)


    def __init__(self):
        super().__init__()
        self.lrServoMS = self.execute_command(Command.lr, -1)[0]
        self.udServoMS = self.execute_command(Command.ud, -1)[0]
        return

    def execute_command(self, command, *params):
        arduino_command = "{0} {1}".format(command, *params)
        return params

    def set_lr_servo(self, ms):
        self.lrServoMS = int(self.execute_command(Command.lr, ms)[0])
        self.lr_servo_changed.emit(self.lrServoMS)

    def set_ud_servo(self, ms):
        self.udServoMS = int(self.execute_command(Command.ud, ms)[0])
        self.ud_servo_changed.emit(self.udServoMS)

    def temperature(self, lr_ms, ud_ms):
        self.execute_command(Command.t, lr_ms, ud_ms)
        return 120+random()*10


arduinoCtrl = ArduinoCtrl()


