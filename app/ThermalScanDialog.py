import json
import os.path
import glob

from PyQt5.QtCore import (QObject, pyqtSignal, Qt, QThread, pyqtSlot)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *

import cv2
from PyQt5.QtWidgets import QProgressDialog, QApplication, QListWidgetItem

from ArduinoCtrl import ArduinoCtrl
from RectangeScanJob import RectangleScanJob
from SettingsDialog import SettingsDialog
from Ui_ThermalScanDialog import Ui_ThermalScanDialog
import Settings

class ThermalScanDialog(QtWidgets.QDialog, Ui_ThermalScanDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.pushButton_Calibrate.clicked.connect(self.handle_calibrate)
        self.pushButton_Close.clicked.connect(self.handle_close)
        self.pushButton_Scan.clicked.connect(self.handle_scan)
        self.pushButton_Settings.clicked.connect(self.handle_settings)
        self.list_images.itemDoubleClicked.connect(self.handle_show_image)

        # read settings
        loaded_settings = {}
        if (os.path.isfile('settings.json')):
            with open('settings.json', 'r') as f:
                loaded_settings = json.load(f)

        Settings.settings.update(loaded_settings)


        image_file = r'../image_processing/edge_detection/pic3.jpg'
        self.cvImage = cv2.imread(image_file)
        height, width, bytes_per_component = self.cvImage.shape
        bytes_per_line = bytes_per_component * width

        self.cap = cv2.VideoCapture(0)

        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        self.mQImage = QImage(self.cvImage, width, height,
                              bytes_per_line, QImage.Format_RGB888)
        self.mQPixmap = QPixmap.fromImage(self.mQImage)

        self.mainImage.resizeEvent = self.image_resize_event

        self.mArduinoCtrl = ArduinoCtrl()
        self.mSettingsDialog = None

        self.directory = "images"
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.fill_images_list()

    def fill_images_list(self):
        self.list_images.clear()
        images = glob.glob(self.directory + '/*.jpg')
        for image in images:
            self.list_images.addItem(os.path.basename(image))

    def load_and_show_image(self, image_file):
        self.cvImage = cv2.imread(self.directory + '/' + image_file)
        height, width, bytes_per_component = self.cvImage.shape
        bytes_per_line = bytes_per_component * width

        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        self.mQImage = QImage(self.cvImage, width, height,
                              bytes_per_line, QImage.Format_RGB888)
        self.mQPixmap = QPixmap.fromImage(self.mQImage)
        ww = self.mainImage.width() - 2
        hh = self.mainImage.height() - 2
        self.mainImage.setPixmap(
            self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))
        self.mainImage.repaint()

    def image_resize_event(self, event):
        ww = self.mainImage.width() - 2
        hh = self.mainImage.height() - 2
        self.mainImage.setPixmap(
            self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))

    def handle_scan(self, param):
        rectangleScanJob = RectangleScanJob()
        rectangleScanJob.start()

    def test(self):
        ret, frame = self.cap.read()
        self.cvImage = frame

        height, width, bytes_per_component = self.cvImage.shape
        bytes_per_line = bytes_per_component * width

        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        self.mQImage = QImage(self.cvImage, width, height,
                              bytes_per_line, QImage.Format_RGB888)
        self.mQPixmap = QPixmap.fromImage(self.mQImage)
        ww = self.mainImage.width() - 2
        hh = self.mainImage.height() - 2
        self.mainImage.setPixmap(
            self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))
        self.mainImage.repaint()
        pass

    @pyqtSlot()
    def handle_calibrate(self):
        return

    @pyqtSlot()
    def handle_settings(self):
        self.mSettingsDialog = SettingsDialog(self)
        self.mSettingsDialog.exec_()

    @pyqtSlot(QListWidgetItem)
    def handle_show_image(self, item):
        image_file = item.text()
        self.load_and_show_image(image_file)
        return

    @pyqtSlot()
    def handle_close(self):
        exit()

