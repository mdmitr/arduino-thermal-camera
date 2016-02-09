from PyQt5.QtCore import QThread, pyqtSignal
from ArduinoCtrl import arduinoCtrl
import Settings

class RectangleScanJob(QThread):

    new_value = pyqtSignal(int, int, float)
    progress = pyqtSignal(int)
    phase_completed = pyqtSignal()

    def __init__(self):
        super().__init__()

        s = Settings.settings

        self.lr_min_ms = s['lrServoMin']
        self.lr_max_ms = s['lrServoMax']
        self.lr_step_ms = s['lrStep']

        self.ud_min_ms = s['udServoMin']
        self.ud_max_ms = s['udServoMax']
        self.ud_step_ms = s['udStep']

        self.gridColumns = int(abs(self.lr_max_ms-self.lr_min_ms)/self.lr_step_ms)+1
        self.gridRows = int(abs(self.ud_max_ms-self.ud_min_ms)/self.ud_step_ms)+1

        self.lr_step_ms = self.lr_step_ms if self.lr_max_ms > self.lr_min_ms else -self.lr_step_ms
        self.ud_step_ms = self.ud_step_ms if self.ud_max_ms > self.ud_min_ms else -self.ud_step_ms

    def __del__(self):
        self.wait()

    def row2ms(self, row):
        ms = self.ud_min_ms + row*self.ud_step_ms
        return ms

    def col2ms(self, col):
        ms = self.lr_min_ms + col*self.lr_step_ms
        return ms

    def run(self):

        I_forward = range(0, self.gridColumns)
        I_backward = range(self.gridColumns-1, -1, -1)
        cnt = 0
        for j in range(self.gridRows):
            rowMS = self.row2ms(j)
            arduinoCtrl.set_ud_servo(rowMS)
            I = []
            for i in I_forward:# if j%2 is 0 else I_backward:
                colMS = self.col2ms(i)

                arduinoCtrl.set_lr_servo(colMS)
                acolMS = arduinoCtrl.get_lr_servo()
                if acolMS != colMS:
                    print ('{0},{1}'.format(colMS, acolMS))
                temp = arduinoCtrl.temperature()
                print('A[{},{}]={}'.format(j, i, temp))
                self.new_value.emit(i, j, temp)
                cnt += 1

               # if cnt % 50 is 0:
                self.progress.emit(cnt)

        self.progress.emit(100000)