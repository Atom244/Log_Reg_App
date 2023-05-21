import os.path
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import *
from PyQt5 import QtPrintSupport
from PyQt5 import QtGui, QtCore
from ui import Ui_Form
import sys

class Autorization(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui = Ui_Form()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.reg)
        self.pushButton_2.clicked.connect(self.log_pas)


    def log_pas(self):
        global entities
        log1 = self.login.text()
        pas1 = self.password.text()
        if self.login.text() == '' or self.password.text() == '':
            self.info.setText('')
            self.info_2.setText('Не введены все данные')
            return
        entities = (log1, pas1)
        con = sqlite3.connect('mtdb.db')
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
        login TEXT,
        password TEXT
        )
        """)
        cur.execute("SELECT * FROM users")
        for i in cur.fetchall():
            if i[0] == log1:
                self.info.setText('')
                self.info_2.setText('Такой логин уже существует')
                return


        cur.execute("""
        INSERT INTO users(login, password) VALUES(?,?)
        """, entities)
        con.commit()

    def reg(self):

        log1 = self.login.text()
        pas1 = self.password.text()

        con = sqlite3.connect('mtdb.db')
        cur = con.cursor()
        cur.execute(f"SELECT * FROM users WHERE login='{log1}'")
        value = cur.fetchall()
        if self.login.text() == '' or self.password.text() == '':
            self.info.setText('')
            self.info_2.setText('Не введены все данные')
            return
        if value != [] and value[0][1] == pas1:
            self.info_2.setText('Успешный вход')
            self.info.setText('')
        else:
            self.info_2.setText('')
            self.info.setText('Проверьте правильность ввода\n'
                              'данных')
            return

        con.commit()
        cur.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Autorization()
    win.show()
    sys.exit(app.exec_())