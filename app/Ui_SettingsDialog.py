# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(361, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb_arduino_comport = QtWidgets.QComboBox(SettingsDialog)
        self.cb_arduino_comport.setObjectName("cb_arduino_comport")
        self.horizontalLayout.addWidget(self.cb_arduino_comport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 321, 115))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spin_lrMax = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spin_lrMax.setObjectName("spin_lrMax")
        self.gridLayout_2.addWidget(self.spin_lrMax, 1, 1, 1, 1)
        self.spin_lrMin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_lrMin.sizePolicy().hasHeightForWidth())
        self.spin_lrMin.setSizePolicy(sizePolicy)
        self.spin_lrMin.setMinimumSize(QtCore.QSize(100, 0))
        self.spin_lrMin.setObjectName("spin_lrMin")
        self.gridLayout_2.addWidget(self.spin_lrMin, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.spin_lrCenter = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spin_lrCenter.setObjectName("spin_lrCenter")
        self.gridLayout_2.addWidget(self.spin_lrCenter, 2, 1, 1, 1)
        self.pb_test_lrMin = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_test_lrMin.setObjectName("pb_test_lrMin")
        self.gridLayout_2.addWidget(self.pb_test_lrMin, 0, 3, 1, 1)
        self.pb_test_lrCenter = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_test_lrCenter.setObjectName("pb_test_lrCenter")
        self.gridLayout_2.addWidget(self.pb_test_lrCenter, 2, 3, 1, 1)
        self.pb_test_lrMax = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pb_test_lrMax.setObjectName("pb_test_lrMax")
        self.gridLayout_2.addWidget(self.pb_test_lrMax, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 321, 109))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spin_udMax = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spin_udMax.setObjectName("spin_udMax")
        self.gridLayout_3.addWidget(self.spin_udMax, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.spin_udMin = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_udMin.sizePolicy().hasHeightForWidth())
        self.spin_udMin.setSizePolicy(sizePolicy)
        self.spin_udMin.setMinimumSize(QtCore.QSize(100, 0))
        self.spin_udMin.setObjectName("spin_udMin")
        self.gridLayout_3.addWidget(self.spin_udMin, 0, 1, 1, 1)
        self.spin_udCenter = QtWidgets.QSpinBox(self.gridLayoutWidget_2)
        self.spin_udCenter.setObjectName("spin_udCenter")
        self.gridLayout_3.addWidget(self.spin_udCenter, 2, 1, 1, 1)
        self.pb_test_udCenter = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_test_udCenter.setObjectName("pb_test_udCenter")
        self.gridLayout_3.addWidget(self.pb_test_udCenter, 2, 3, 1, 1)
        self.pb_test_udMax = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_test_udMax.setObjectName("pb_test_udMax")
        self.gridLayout_3.addWidget(self.pb_test_udMax, 1, 3, 1, 1)
        self.pb_test_udMin = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pb_test_udMin.setObjectName("pb_test_udMin")
        self.gridLayout_3.addWidget(self.pb_test_udMin, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.label.setText(_translate("SettingsDialog", "Connect to Arduino via"))
        self.groupBox.setTitle(_translate("SettingsDialog", "Left-Right Servo"))
        self.pb_test_lrMin.setText(_translate("SettingsDialog", "Test"))
        self.pb_test_lrCenter.setText(_translate("SettingsDialog", "Test"))
        self.pb_test_lrMax.setText(_translate("SettingsDialog", "Test"))
        self.label_2.setText(_translate("SettingsDialog", "Minimum microseconds"))
        self.label_3.setText(_translate("SettingsDialog", "Maximum microseconds"))
        self.label_4.setText(_translate("SettingsDialog", "Center microseconds"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Up-Down Servo"))
        self.pb_test_udCenter.setText(_translate("SettingsDialog", "Test"))
        self.pb_test_udMax.setText(_translate("SettingsDialog", "Test"))
        self.pb_test_udMin.setText(_translate("SettingsDialog", "Test"))
        self.label_5.setText(_translate("SettingsDialog", "Minimum microseconds"))
        self.label_6.setText(_translate("SettingsDialog", "Maximum microseconds"))
        self.label_7.setText(_translate("SettingsDialog", "Center microseconds"))

