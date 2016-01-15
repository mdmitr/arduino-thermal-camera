from PyQt5.QtCore import QThread, pyqtSignal
from ArduinoCtrl import arduinoCtrl
import Settings

class RectangleScanJob(QThread):

    new_value = pyqtSignal(int, int, float)

    def __init__(self):
        super().__init__()

        s = Settings.settings

        self.lr_min_ms = s['lrServoMin'] if not s['lrSwapDirection'] else s['lrServoMax']
        self.lr_max_ms = s['lrServoMax'] if not s['lrSwapDirection'] else s['lrServoMin']
        self.lr_step_ms = 1 if self.lr_max_ms > self.lr_min_ms else -1

        self.ud_min_ms = s['udServoMin'] if not s['udSwapDirection'] else s['udServoMax']
        self.ud_max_ms = s['udServoMax'] if not s['udSwapDirection'] else s['udServoMin']
        self.ud_step_ms = 1 if self.ud_max_ms > self.ud_min_ms else -1

    def __del__(self):
        self.wait()

    def run(self):

        for ud_ms in range(self.ud_min_ms, self.ud_max_ms, self.ud_step_ms):
            for lr_ms in range(self.lr_min_ms, self.lr_max_ms, self.lr_step_ms):
                temp = arduinoCtrl.temperature(lr_ms, ud_ms)
                self.new_value.emit(lr_ms, ud_ms, temp)

        return
