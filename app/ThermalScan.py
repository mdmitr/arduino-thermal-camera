from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtWidgets

import ui_ThermalScan

class Ui_ThermalScanDialog(QtWidgets.QDialog, ui_ThermalScan.Ui_ThermalScanDialog):

	def __init__(self, parent=None):
		super(Ui_ThermalScanDialog, self).__init__(parent)
		self.setupUi(self)
		print("dsfsdfsdf")
		self.pushButton_Close.clicked.connect(self.handle_Close)

	def ScanButtonPressed(self, param):
		pass

	def handle_Close(self):
		print("Sdfsdf")
