from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtWidgets

import cv2

import ui_ThermalScan

class Ui_ThermalScanDialog(QtWidgets.QDialog, ui_ThermalScan.Ui_ThermalScanDialog):

	def __init__(self, parent=None):
		super(Ui_ThermalScanDialog, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_Calibrate.clicked.connect(self.handle_Calibrate)
		self.pushButton_Close.clicked.connect(self.handle_Close)

	def ScanButtonPressed(self, param):
		pass

	def handle_Calibrate(self):
		print("Calibrate")

	def handle_Close(self):
		print("Sdfsdf")
