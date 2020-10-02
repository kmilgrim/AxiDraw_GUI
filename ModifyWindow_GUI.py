# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyWindow_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
from pathlib import Path
import sys
import pickle
import os
from pyaxidraw import axidraw
# import csv
# from pyaxidraw import axidraw
# from PyQt5.QtWidgets import *
# app = QApplication([])
# app.setStyle('Fusion')

# makes GUI correct size for higher screen resolution

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class Ui_ModifyWindow(QMainWindow):
    def setupUi(self, ModifyWindow):
        # initialize some variables here so when they are changed in the modify
        # window we can track and use the changes in the main window.
        self.rowNum_1 = 2
        self.rowNum_2 = 2
        self.rowNum_3 = 2
        self.colNum = 11
        self.startPos = 'L'

        ModifyWindow.setObjectName("ModifyWindow")
        ModifyWindow.resize(531, 477)
        self.centralwidget = QtWidgets.QWidget(ModifyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 261, 16))
        font_12 = QtGui.QFont()
        font_12.setFamily("Yu Gothic UI Light")
        font_12.setPointSize(12)
        self.label_2.setFont(font_12)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 501, 31))
        self.label_3.setFont(font_12)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 391, 31))
        self.label_4.setFont(font_12)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(10, 160, 42, 22))
        font_10 = QtGui.QFont()
        font_10.setFamily("Yu Gothic UI Light")
        font_10.setPointSize(10)
        self.spinBox.setFont(font_10)
        self.spinBox.setMaximum(6)
        self.spinBox.setProperty("value", 2)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(80, 160, 42, 22))
        self.spinBox_2.setFont(font_10)
        self.spinBox_2.setMaximum(6)
        self.spinBox_2.setProperty("value", 2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(150, 160, 42, 22))
        self.spinBox_3.setFont(font_10)
        self.spinBox_3.setMaximum(6)
        self.spinBox_3.setProperty("value", 2)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 47, 14))
        font_sb10 = QtGui.QFont()
        font_sb10.setFamily("Yu Gothic UI Semibold")
        font_sb10.setPointSize(10)
        font_sb10.setBold(True)
        font_sb10.setWeight(75)
        self.label_5.setFont(font_sb10)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 130, 47, 14))
        self.label_6.setFont(font_sb10)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 130, 47, 14))
        self.label_7.setFont(font_sb10)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 160, 281, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(10, 240, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(11)
        self.spinBox_4.setProperty("value", 11)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 240, 431, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 320, 141, 18))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.clickBox)

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 340, 151, 18))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.clickBox_2)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 340, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(130, 320, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 380, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        ModifyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 22))
        self.menubar.setObjectName("menubar")
        ModifyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifyWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyWindow)
        QtCore.QMetaObject.connectSlotsByName(ModifyWindow)

    def retranslateUi(self, ModifyWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyWindow.setWindowTitle(_translate("ModifyWindow", "Modify"))
        self.label.setText(_translate("ModifyWindow", "AxiDraw Spotting Experiment"))
        self.label_2.setText(_translate("ModifyWindow", "Experiment Modification Window"))
        self.label_3.setText(_translate("ModifyWindow", "Number of Rows for each Pen Delay Setting (default: 2):"))
        self.label_4.setText(_translate("ModifyWindow", "Columns of spots for each pen delay setting (default, 11):"))
        self.label_5.setText(_translate("ModifyWindow", "1"))
        self.label_6.setText(_translate("ModifyWindow", "2"))
        self.label_7.setText(_translate("ModifyWindow", "3"))
        self.label_8.setText(_translate("ModifyWindow", "*The total number of rows may not exceed 6."))
        self.label_9.setText(_translate("ModifyWindow", "*Will be same number of columns for each pen delay, may not exceed 11."))
        self.label_10.setText(_translate("ModifyWindow", "Starting Place:"))
        self.checkBox.setText(_translate("ModifyWindow", "Top left corner"))
        self.checkBox_2.setText(_translate("ModifyWindow", "Top right corner"))
        self.label_11.setText(_translate("ModifyWindow", "*Axidraw will spot to the left"))
        self.label_12.setText(_translate("ModifyWindow", "*AxiDraw will spot to the right"))
        self.pushButton.setText(_translate("ModifyWindow", "Return"))
        self.pushButton_2.setText(_translate("ModifyWindow", "Save Settings"))

        self.pushButton_2.clicked.connect(self.saveSettings)

    def saveSettings(self):
        self.rowNum_1 = int(self.spinBox.text())
        self.rowNum_2 = int(self.spinBox_2.text())
        self.rowNum_3 = int(self.spinBox_3.text())
        self.colNum = int(self.spinBox_4.text())

    def clickBox(self, state): # need to look at variables
        if state == QtCore.Qt.Checked:
            print('Checked')
            cb1 = True
        else:
            print('Unchecked')
            cb2 = False
        return cb1
    def clickBox_2(self, state):
        if state == QtCore.Qt.Checked:
            print('2 Checked')
            cb2 = True
        else:
            print('2 Unchecked')
            cb2 = False
        return cb2

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModifyWindow = QtWidgets.QMainWindow()
    ui = Ui_ModifyWindow()
    ui.setupUi(ModifyWindow)
    ModifyWindow.show()
    sys.exit(app.exec_())
