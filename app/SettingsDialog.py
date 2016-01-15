from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialogButtonBox, QProgressDialog

import json

from ArduinoCtrl import arduinoCtrl
from CalibrateServoJob import CalibrateServoJob
from Ui_SettingsDialog import Ui_SettingsDialog
import Settings

class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.handle_btnOk)
        self.btn_lrCalibrate.clicked.connect(self.handle_lrCalibrate)
        self.btn_udCalibrate.clicked.connect(self.handle_udCalibrate)

        self.setServoSpinMinMax(self.spin_lrMin)
        self.setServoSpinMinMax(self.spin_lrMax)
        self.setServoSpinMinMax(self.spin_lrCenter)
        self.setServoSpinMinMax(self.spin_udMin)
        self.setServoSpinMinMax(self.spin_udMax)
        self.setServoSpinMinMax(self.spin_udCenter)

        self.spin_lrMin.setValue(Settings.settings['lrServoMin'])
        self.spin_lrMax.setValue(Settings.settings['lrServoMax'])
        self.spin_lrCenter.setValue(Settings.settings['lrServoCenter'])
        self.cb_lrSwap.setChecked(Settings.settings['lrSwapDirection'])
        
        self.spin_udMin.setValue(Settings.settings['udServoMin'])
        self.spin_udMax.setValue(Settings.settings['udServoMax'])
        self.spin_udCenter.setValue(Settings.settings['udServoCenter'])
        self.cb_udSwap.setChecked(Settings.settings['udSwapDirection'])

    def setServoSpinMinMax(self, spin):
        spin.setMinimum(Settings.settings['servoMinMicroseconds'])
        spin.setMaximum(Settings.settings['servoMaxMicroseconds'])

    @pyqtSlot()
    def handle_btnOk(self):
        """
            Saving settings
        """
        Settings.settings['lrServoMin'] = self.spin_lrMin.value()
        Settings.settings['lrServoMax'] = self.spin_lrMax.value()
        Settings.settings['lrServoCenter'] = self.spin_lrCenter.value()
        Settings.settings['lrSwapDirection'] = self.cb_lrSwap.isChecked()
        
        Settings.settings['udServoMin'] = self.spin_udMin.value()
        Settings.settings['udServoMax'] = self.spin_udMax.value()
        Settings.settings['udServoCenter'] = self.spin_udCenter.value()
        Settings.settings['udSwapDirection'] = self.cb_udSwap.isChecked()

        with open('settings.json', 'w') as f:
            json.dump(Settings.settings, f)

    def servo_calibrate(self, servo_name):
        """
            Moving servo from minimum to maximum angle. waiting for user to abort process.
        :rtype: int
        """

        if servo_name == 'lr':
            min_ms = self.spin_lrMin.value()
            max_ms = self.spin_lrMax.value()
            if self.cb_lrSwap.isChecked():
                min_ms, max_ms = max_ms, min_ms
        else:
            min_ms = self.spin_udMin.value()
            max_ms = self.spin_udMax.value()
            if self.cb_udSwap.isChecked():
                min_ms, max_ms = max_ms, min_ms

        calibrate_thread = CalibrateServoJob(servo_name, min_ms, max_ms)
        progress = QProgressDialog('Calibrating servo', 'Stop', min_ms, max_ms)
        arduinoCtrl.lr_servo_changed.connect(progress.setValue)
        arduinoCtrl.ud_servo_changed.connect(progress.setValue)
        calibrate_thread.start()
        progress.exec_()
        calibrate_thread.terminate()

        if progress.wasCanceled():
            if servo_name == 'lr':
                return arduinoCtrl.lrServoMS
            else:
                return arduinoCtrl.udServoMS

        return -1

    @pyqtSlot()
    def handle_lrCalibrate(self):
        value = self.servo_calibrate('lr')
        if value == -1:
            return
        if self.rb_lrMin.isChecked():
            self.spin_lrMin.setValue(value)
        if self.rb_lrMax.isChecked():
            self.spin_lrMax.setValue(value)
        if self.rb_lrCenter.isChecked():
            self.spin_lrCenter.setValue(value)

    @pyqtSlot()
    def handle_udCalibrate(self):
        value = self.servo_calibrate('ud')
        if value == -1:
            return
        if self.rb_udMin.isChecked():
            self.spin_udMin.setValue(value)
        if self.rb_udMax.isChecked():
            self.spin_udMax.setValue(value)
        if self.rb_udCenter.isChecked():
            self.spin_udCenter.setValue(value)
        
    
