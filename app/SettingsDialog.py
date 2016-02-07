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
        self.pb_test_udMin.clicked.connect(self.handle_test_udMin)
        self.pb_test_udMax.clicked.connect(self.handle_test_udMax)
        self.pb_test_udCenter.clicked.connect(self.handle_test_udCenter)


        self.setServoSpinMinMax(self.spin_lrMin)
        self.setServoSpinMinMax(self.spin_lrMax)
        self.setServoSpinMinMax(self.spin_lrCenter)
        self.setServoSpinMinMax(self.spin_udMin)
        self.setServoSpinMinMax(self.spin_udMax)
        self.setServoSpinMinMax(self.spin_udCenter)
        self.spin_lrStep.setMinimum(1)
        self.spin_lrStep.setMaximum(100)
        self.spin_udStep.setMinimum(1)
        self.spin_udStep.setMaximum(100)

        self.spin_lrMin.setValue(Settings.settings['lrServoMin'])
        self.spin_lrMax.setValue(Settings.settings['lrServoMax'])
        self.spin_lrCenter.setValue(Settings.settings['lrServoCenter'])
        self.spin_lrStep.setValue(Settings.settings['lrStep'])

        self.spin_udMin.setValue(Settings.settings['udServoMin'])
        self.spin_udMax.setValue(Settings.settings['udServoMax'])
        self.spin_udCenter.setValue(Settings.settings['udServoCenter'])
        self.spin_udStep.setValue(Settings.settings['udStep'])

        for i in range(4):
            self.cb_arduino_comport.addItem("COM{0}".format(i+1))
        self.cb_arduino_comport.setCurrentIndex(Settings.settings['comport']-1)

        self.update_grid_info()

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
        Settings.settings['lrStep'] = self.spin_lrStep.value()

        Settings.settings['udServoMin'] = self.spin_udMin.value()
        Settings.settings['udServoMax'] = self.spin_udMax.value()
        Settings.settings['udServoCenter'] = self.spin_udCenter.value()
        Settings.settings['udStep'] = self.spin_udStep.value()

        Settings.settings['comport'] = self.cb_arduino_comport.currentIndex()+1

        with open('settings.json', 'w') as f:
            json.dump(Settings.settings, f)


    @pyqtSlot()
    def handle_test_lrMin(self):
        value = self.spin_lrMin.value()
        arduinoCtrl.set_lr_servo(value)
        self.update_grid_info()

    @pyqtSlot()
    def handle_test_lrMax(self):
        value = self.spin_lrMax.value()
        arduinoCtrl.set_lr_servo(value)
        self.update_grid_info()

    @pyqtSlot()
    def handle_test_lrCenter(self):
        value = self.spin_lrCenter.value()
        arduinoCtrl.set_lr_servo(value)
        self.update_grid_info()

    @pyqtSlot()
    def handle_test_udMin(self):
        value = self.spin_udMin.value()
        arduinoCtrl.set_ud_servo(value)
        self.update_grid_info()

    @pyqtSlot()
    def handle_test_udMax(self):
        value = self.spin_udMax.value()
        arduinoCtrl.set_ud_servo(value)
        self.update_grid_info()

    @pyqtSlot()
    def handle_test_udCenter(self):
        value = self.spin_udCenter.value()
        arduinoCtrl.set_ud_servo(value)
        self.update_grid_info()

    def update_grid_info(self):
        self.label_grid_info.setText("hello")