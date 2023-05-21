# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logreg2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 600)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(160, 100, 450, 430))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 221, 430))
        self.label.setStyleSheet("background-image: url(desert.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(220, 0, 231, 431))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 48,170), stop:1 rgba(36, 59, 85,170));\n"
"border-bottom-right-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, -1, 221, 431))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border-top-left-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(260, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255, 210);")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.login = QtWidgets.QLineEdit(self.widget)
        self.login.setGeometry(QtCore.QRect(240, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color:rgb(255, 255, 255, 80);\n"
"color: rgb(0, 0, 0, 120);\n"
"border: none;\n"
"\n"
"padding-bottom: 2px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-radius:10px;")
        self.login.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(240, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgb(255, 255, 255, 80);\n"
"color: rgb(0, 0, 0, 120);\n"
"border: none;\n"
"\n"
"padding-bottom: 2px;\n"
"padding-left:5px;\n"
"padding-right:5px;\n"
"border-radius:10px;")
        self.password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(240, 240, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 48, 170), stop:1 rgba(36, 59, 85, 170));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 40, 220), stop:1 rgba(36, 59, 80, 220));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 48, 100), stop:1 rgba(36, 59, 85, 100));\n"
"    \n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 310, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 48, 170), stop:1 rgba(36, 59, 85, 170));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 40, 220), stop:1 rgba(36, 59, 80, 220));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 30, 48, 100), stop:1 rgba(36, 59, 85, 100));\n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.info = QtWidgets.QLabel(self.widget)
        self.info.setGeometry(QtCore.QRect(250, 370, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info.setFont(font)
        self.info.setStyleSheet("color: rgb(240, 240, 240, 100);")
        self.info.setText("")
        self.info.resize(181, 41)
        self.info.setObjectName("info")

        self.info_2 = QtWidgets.QLabel(self.widget)
        self.info_2.setGeometry(QtCore.QRect(240, 210, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info_2.setFont(font)
        self.info_2.setStyleSheet("color: rgb(240, 240, 240, 100);")
        self.info_2.setText("")
        self.info_2.setObjectName("info_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Авторизация</span></p></body></html>"))
        self.login.setPlaceholderText(_translate("Form", "Введите логин"))
        self.password.setPlaceholderText(_translate("Form", "Введите пароль"))
        self.pushButton.setText(_translate("Form", "Вход"))
        self.pushButton_2.setText(_translate("Form", "Регистрация"))

