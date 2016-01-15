from PyQt5.QtCore import QThread

from ArduinoCtrl import arduinoCtrl

class CalibrateServo(QThread):
    def __init__(self, servo_name, start_ms, stop_ms):
        super().__init__()
        self.servo_name = servo_name
        self.start_ms = start_ms
        self.stop_ms = stop_ms
        return

    def __del__(self):
        self.wait()

    def set_servo(self, ms):
        if self.servo_name == 'lr':
            value = arduinoCtrl.set_lr_servo(ms)
        else:
            value = arduinoCtrl.set_ud_servo(ms)
        return value

    def run(self):
        for ms in range(self.start_ms, self.stop_ms, max(1, (self.stop_ms-self.start_ms)/5000)):
            self.set_servo(ms)
            self.usleep(500)
        self.set_servo(self.stop_ms)

