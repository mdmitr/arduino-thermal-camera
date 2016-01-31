from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialogButtonBox, QProgressDialog

import json

from ArduinoCtrl import arduinoCtrl
from Ui_SettingsDialog import Ui_SettingsDialog
import Settings

class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.handle_btnOk)
        self.pb_test_lrMin.clicked.connect(self.handle_test_lrMin)
        self.pb_test_lrMax.clicked.connect(self.handle_test_lrMax)
        self.pb_test_lrCenter.clicked.connect(self.handle_test_lrCenter)

        self.setServoSpinMinMax(self.spin_lrMin)
        self.setServoSpinMinMax(self.spin_lrMax)
        self.setServoSpinMinMax(self.spin_lrCenter)
        self.setServoSpinMinMax(self.spin_udMin)
        self.setServoSpinMinMax(self.spin_udMax)
        self.setServoSpinMinMax(self.spin_udCenter)

        self.spin_lrMin.setValue(Settings.settings['lrServoMin'])
        self.spin_lrMax.setValue(Settings.settings['lrServoMax'])
        self.spin_lrCenter.setValue(Settings.settings['lrServoCenter'])

        self.spin_udMin.setValue(Settings.settings['udServoMin'])
        self.spin_udMax.setValue(Settings.settings['udServoMax'])
        self.spin_udCenter.setValue(Settings.settings['udServoCenter'])

        for i in range(4):
            self.cb_arduino_comport.addItem("COM{0}".format(i+1))
        self.cb_arduino_comport.setCurrentIndex(Settings.settings['comport']-1)

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

        Settings.settings['udServoMin'] = self.spin_udMin.value()
        Settings.settings['udServoMax'] = self.spin_udMax.value()
        Settings.settings['udServoCenter'] = self.spin_udCenter.value()

        Settings.settings['comport'] = self.cb_arduino_comport.currentIndex()+1

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

        return -1

    @pyqtSlot()
    def handle_test_lrMin(self):
        value = self.spin_lrMin.value()
        arduinoCtrl.set_lr_servo(value);

    @pyqtSlot()
    def handle_test_lrMax(self):
        value = self.spin_lrMax.value()
        arduinoCtrl.set_lr_servo(value);

    @pyqtSlot()
    def handle_test_lrCenter(self):
        value = self.spin_lrCenter.value()
        arduinoCtrl.set_lr_servo(value);

