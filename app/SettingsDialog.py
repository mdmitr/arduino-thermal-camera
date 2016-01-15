from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox

import json

from Ui_SettingsDialog import Ui_SettingsDialog
from Settings import settings

class SettingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.handle_btnOk)

        self.setServoSpinMinMax(self.spin_lrMin)
        self.setServoSpinMinMax(self.spin_lrMax)
        self.setServoSpinMinMax(self.spin_lrCenter)
        self.setServoSpinMinMax(self.spin_udMin)
        self.setServoSpinMinMax(self.spin_udMax)
        self.setServoSpinMinMax(self.spin_udCenter)

        self.spin_lrMin.setValue(settings['lrServoMin'])
        self.spin_lrMax.setValue(settings['lrServoMax'])
        self.spin_lrCenter.setValue(settings['lrServoCenter'])
        self.cb_lrSwap.setChecked(settings['lrSwapDirection'])
        
        self.spin_udMin.setValue(settings['udServoMin'])
        self.spin_udMax.setValue(settings['udServoMax'])
        self.spin_udCenter.setValue(settings['udServoCenter'])
        self.cb_udSwap.setChecked(settings['udSwapDirection'])

    def setServoSpinMinMax(self, spin):
        spin.setMinimum(settings['servoMinMicroseconds'])
        spin.setMaximum(settings['servoMaxMicroseconds'])

    def handle_btnOk(self):
        """
            Saving settings
        """
        settings['lrServoMin'] = self.spin_lrMin.value()
        settings['lrServoMax'] = self.spin_lrMax.value()
        settings['lrServoCenter'] = self.spin_lrCenter.value()
        settings['lrSwapDirection'] = self.cb_lrSwap.isChecked()
        
        settings['udServoMin'] = self.spin_udMin.value()
        settings['udServoMax'] = self.spin_udMax.value()
        settings['udServoCenter'] = self.spin_udCenter.value()
        settings['udSwapDirection'] = self.cb_udSwap.isChecked()

        with open('settings.json', 'w') as f:
            json.dump(settings, f)


