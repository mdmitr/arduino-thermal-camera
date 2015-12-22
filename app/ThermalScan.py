from PyQt5.QtCore import (QObject, pyqtSignal, Qt)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *

import cv2

import ui_ThermalScan

class Ui_ThermalScanDialog(QtWidgets.QDialog, ui_ThermalScan.Ui_ThermalScanDialog):

	def __init__(self, parent=None):
		super(Ui_ThermalScanDialog, self).__init__(parent)
		self.setupUi(self)
		self.pushButton_Calibrate.clicked.connect(self.handle_Calibrate)
		self.pushButton_Close.clicked.connect(self.handle_Close)

		image_file = r'../image_processing/edge_detection/pic3.jpg'
		self.cvImage = cv2.imread(image_file)
		height, width, bytesPerComponent = self.cvImage.shape
		bytesPerLine = bytesPerComponent * width

		cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
		self.mQImage = QImage(self.cvImage, width, height, bytesPerLine, QImage.Format_RGB888)
		self.mQPixmap = QPixmap.fromImage(self.mQImage)

		self.mainImage.resizeEvent = self.imageResizeEvent

	def imageResizeEvent(self, event):
		ww = self.mainImage.width()-2
		hh = self.mainImage.height()-2
		self.mainImage.setPixmap(self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))

	def ScanButtonPressed(self, param):
		pass

	def handle_Calibrate(self):
		print("Calibrate")

	def handle_Close(self):

		ww = self.mainImage.width() - 2
		hh = self.mainImage.height() - 2
		self.mainImage.setPixmap(self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))
		
		self.mainImage.repaint()
		print("Sdfsdf")

	
