# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ThremalScan.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ThermalScanDialog(object):
    def setupUi(self, ThermalScanDialog):
        ThermalScanDialog.setObjectName("ThermalScanDialog")
        ThermalScanDialog.resize(820, 557)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ThermalScanDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.ImageLayout = QtWidgets.QVBoxLayout()
        self.ImageLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.ImageLayout.setObjectName("ImageLayout")
        self.mainImage = QtWidgets.QLabel(ThermalScanDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainImage.sizePolicy().hasHeightForWidth())
        self.mainImage.setSizePolicy(sizePolicy)
        self.mainImage.setMinimumSize(QtCore.QSize(1, 1))
        self.mainImage.setMouseTracking(True)
        self.mainImage.setAcceptDrops(True)
        self.mainImage.setAutoFillBackground(True)
        self.mainImage.setFrameShape(QtWidgets.QFrame.Box)
        self.mainImage.setText("")
        self.mainImage.setAlignment(QtCore.Qt.AlignCenter)
        self.mainImage.setObjectName("mainImage")
        self.ImageLayout.addWidget(self.mainImage)
        self.mainLayout.addLayout(self.ImageLayout)
        self.ButotnsLayout = QtWidgets.QHBoxLayout()
        self.ButotnsLayout.setObjectName("ButotnsLayout")
        self.pushButton_Analyze = QtWidgets.QPushButton(ThermalScanDialog)
        self.pushButton_Analyze.setObjectName("pushButton_Analyze")
        self.ButotnsLayout.addWidget(self.pushButton_Analyze)
        self.pushButton_Calibrate = QtWidgets.QPushButton(ThermalScanDialog)
        self.pushButton_Calibrate.setObjectName("pushButton_Calibrate")
        self.ButotnsLayout.addWidget(self.pushButton_Calibrate)
        self.pushButton_Scan = QtWidgets.QPushButton(ThermalScanDialog)
        self.pushButton_Scan.setObjectName("pushButton_Scan")
        self.ButotnsLayout.addWidget(self.pushButton_Scan)
        self.pushButton_Close = QtWidgets.QPushButton(ThermalScanDialog)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.ButotnsLayout.addWidget(self.pushButton_Close)
        self.mainLayout.addLayout(self.ButotnsLayout)
        self.mainLayout.setStretch(0, 10)
        self.verticalLayout_2.addLayout(self.mainLayout)

        self.retranslateUi(ThermalScanDialog)
        QtCore.QMetaObject.connectSlotsByName(ThermalScanDialog)

    def retranslateUi(self, ThermalScanDialog):
        _translate = QtCore.QCoreApplication.translate
        ThermalScanDialog.setWindowTitle(_translate("ThermalScanDialog", "Thermal Scanner"))
        self.pushButton_Analyze.setText(_translate("ThermalScanDialog", "Analyze"))
        self.pushButton_Calibrate.setText(_translate("ThermalScanDialog", "Calibrate"))
        self.pushButton_Scan.setText(_translate("ThermalScanDialog", "Scan"))
        self.pushButton_Close.setText(_translate("ThermalScanDialog", "Close"))

