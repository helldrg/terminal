# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'terminal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 366)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(22, 23, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 280, 221, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(61, 63, 69);\n"
"color: rgb(145, 147, 150);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 17, 21, 21))
        self.pushButton.setStyleSheet("\n"
"border-image: url(:/newPrefix/img/settings_ico.png) stretch;\n"
"color: rgb(145, 147, 150);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 250, 431, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 431, 121))
        self.label.setStyleSheet("color: rgb(199, 201, 205);\n"
"background-color: rgb(22, 23, 29);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(450, 120, 91, 22))
        self.comboBox.setStyleSheet("color: rgb(145, 147, 150);\n"
"background-color: rgb(61, 63, 69);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 100, 91, 16))
        self.label_2.setStyleSheet("color: rgb(145, 147, 150);\n"
"background-color: rgb(61, 63, 69);")
        self.label_2.setIndent(5)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 551, 51))
        self.label_3.setStyleSheet("background-color: rgb(36, 37, 43);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Terminal"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.comboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox.setItemText(1, _translate("MainWindow", "115200"))
        self.label_2.setText(_translate("MainWindow", "Baude Rate"))
import font_rc
import image_rc
