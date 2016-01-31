import json
import os.path
import glob

import numpy as np
from numpy import interp
import cv2

from PyQt5.QtCore import (QObject, pyqtSignal, Qt, QThread, pyqtSlot)
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QProgressDialog, QApplication, QListWidgetItem

#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

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

        self.mQPixmap = QPixmap()
        self.mainImage.resizeEvent = self.image_resize_event


        self.mMatrix = None

        # read settings
        loaded_settings = {}
        if (os.path.isfile('settings.json')):
            with open('settings.json', 'r') as f:
                loaded_settings = json.load(f)

        Settings.settings.update(loaded_settings)

        self.sb_minTemp.setValue(Settings.settings['minTemp'])
        self.sb_maxTemp.setValue(Settings.settings['maxTemp'])

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

    def update_pixmap_from_matrix(self):

        max_x = self.mMatrix.shape[0]
        max_y = self.mMatrix.shape[1]

        colorTable = [ qRgb(x, 0, 255-x) for x in range(255) ]

        matr = interp(self.mMatrix, [-30, 150], [0, 256])

        self.mQImage = QImage(self.mMatrix.astype(np.int8).data, max_x, max_y, QImage.Format_Indexed8)
        self.mQImage.setColorTable(colorTable)

        minColor = Qt.blue
        maxColor = Qt.red

        #for j in range(max_y):
        #    for i in range(max_x):
        #        self.mQImage.setPixel(i, j, minColor)
        #self.mQImage.fill(minColor)


        self.mQPixmap = QPixmap.fromImage(self.mQImage)
        self.update_image_from_pixmap()
        return

    def update_image_from_pixmap(self):
        ww = self.mainImage.width() - 2
        hh = self.mainImage.height() - 2
        self.mainImage.setPixmap(
            self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))
        self.mainImage.repaint()

    def load_and_show_image(self, image_file):
        self.cvImage = cv2.imread(self.directory + '/' + image_file)
        height, width, bytes_per_component = self.cvImage.shape
        bytes_per_line = bytes_per_component * width

        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        self.mQImage = QImage(self.cvImage, width, height,
                              bytes_per_line, QImage.Format_RGB888)
        self.mQPixmap = QPixmap.fromImage(self.mQImage)
        self.update_image_from_pixmap()

    def image_resize_event(self, event):
        ww = self.mainImage.width() - 2
        hh = self.mainImage.height() - 2
        self.mainImage.setPixmap(
            self.mQPixmap.scaled(ww, hh, Qt.KeepAspectRatio))

    def test_camera(self):
        ret, frame = self.cap.read()
        self.cvImage = frame

        height, width, bytes_per_component = self.cvImage.shape
        bytes_per_line = bytes_per_component * width

        cv2.cvtColor(self.cvImage, cv2.COLOR_BGR2RGB, self.cvImage)
        self.mQImage = QImage(self.cvImage, width, height,
                              bytes_per_line, QImage.Format_RGB888)
        self.mQPixmap = QPixmap.fromImage(self.mQImage)
        self.update_image_from_pixmap()
        pass

    def handle_scan(self, param):

        ox_len = int(abs(Settings.settings['lrServoMax'] - Settings.settings['lrServoMin']) / Settings.settings['lrStep'])
        oy_len = int(abs(Settings.settings['udServoMax'] - Settings.settings['udServoMin']) / Settings.settings['udStep'])

        total_points = ox_len * oy_len
        progress = QProgressDialog('Scanning thermal image', 'Stop', 0, total_points)

        self.mMatrix = np.zeros((ox_len, oy_len))

        self.mQPixmap = QPixmap(ox_len, oy_len)
        self.mQPixmap.fill()

        rectangleScanJob = RectangleScanJob()
        rectangleScanJob.new_value.connect(self.handle_temperature)
        rectangleScanJob.progress.connect(progress.setValue)
        rectangleScanJob.start()

        progress.exec_()

        if progress.wasCanceled():
            rectangleScanJob.terminate()
            return

        self.update_pixmap_from_matrix()

    def handle_temperature(self, xpos, ypos, temp):

        self.mMatrix[xpos][ypos] = temp

        #self.update_image_from_pixmap()

        return

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

