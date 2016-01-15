from PyQt5.QtCore import QObject, pyqtSignal

class Command:
    lr = 0,  # calls left-right servo setMicroSeconds, or getMicroseconds if parameter is ?
    ud = 1,  # calls up-down servo setMicroSeconds, or getMicroseconds if parameter is ?
    srv = 2, # calls for both servos setMicroSeconds, or getMicroseconds if parameter is ?
    t = 3    # get temperature at current point

class ArduinoCtrl(QObject):

    lr_servo_changed = pyqtSignal(int)
    ud_servo_changed = pyqtSignal(int)


    def __init__(self):
        super().__init__()

        self.lrServoMS = int(self.execute_command(Command.lr, '-1'))
        self.udServoMS = int(self.execute_command(Command.ud, '-1'))
        return

    def execute_command(self, command, params):
        arduino_command = "{0} {1}".format(command, params)
        return params

    def set_lr_servo(self, ms):
        self.lrServoMS = int(self.execute_command(Command.lr, ms))
        self.lr_servo_changed.emit(self.lrServoMS)

    def set_ud_servo(self, ms):
        self.udServoMS = int(self.execute_command(Command.ud, ms))
        self.ud_servo_changed.emit(self.udServoMS)



arduinoCtrl = ArduinoCtrl()


