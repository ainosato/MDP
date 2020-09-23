# -*- coding: utf-8 -*-

import sys

import PyQt5
import sys, pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import *
import tkinter.messagebox

PadUI = '../_uiFiles/keypad.ui'
SaveUI = '../_uiFiles/saved.ui'
MainUI = '../_uiFiles/main.ui'
OutUI = '../_uiFiles/out.ui'
OutcarUI = '../_uiFiles/outcar.ui'

ar = []
carID = []


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(MainUI, self)

        self.in_pushButton.clicked.connect(self.go)
        self.out_pushButton.clicked.connect(self.out)

        self.in_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/입차.png); border:5px solid gray; border-radius:10px;}
                QPushButton:hover{image:url(../image/입차.png); border:3px solid gray;}
            ''')
        self.out_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/out.png); border:5px solid gray; border-radius:10px;}
                QPushButton:hover{image:url(../image/out.png); border:3px solid gray;}
            ''')
        self.service_label.setStyleSheet(
            '''
                 QLabel{image:url(../image/service_label.png); border:0px;}
            '''
        )

    def go(self):
        self.close()
        pad = KeypadDialog()
        pad.exec_()

    def out(self):
        self.close()
        out = outDialog()
        out.exec_()

class Keypad(QDialog):
    def __init__(self):

        QDialog.__init__(self, None)
        uic.loadUi(PadUI, self)
        self.sqlConnect()
        self.num_pushButton_1.clicked.connect(lambda state, button=self.num_pushButton_1: self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button=self.num_pushButton_2: self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button=self.num_pushButton_3: self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button=self.num_pushButton_4: self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button=self.num_pushButton_5: self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button=self.num_pushButton_6: self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button=self.num_pushButton_7: self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button=self.num_pushButton_8: self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button=self.num_pushButton_9: self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button=self.num_pushButton_0: self.NumClicked(state, button))

        self.del_pushButton.clicked.connect(self.Delete)
        self.enter_pushButton.clicked.connect(self.checkAnswer)
        self.home_pushButton.clicked.connect(self.home)

        self.num_pushButton_0.setStyleSheet(
        '''
            QPushButton{image:url(../image/0.png); border:0px;}
            QPushButton:hover{image:url(../image/0.png); border:4px solid gray;}
        ''')
        self.num_pushButton_0.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_1.setStyleSheet(
            '''
                QPushButton{image:url(../image/1.png); border:0px;}
                QPushButton:hover{image:url(../image/1.png); border:4px solid gray;}
            ''')
        self.num_pushButton_1.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_2.setStyleSheet(
            '''
                QPushButton{image:url(../image/2.png); border:0px;}
                QPushButton:hover{image:url(../image/2.png); border:4px solid gray;}
            ''')
        self.num_pushButton_2.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_3.setStyleSheet(
            '''
                QPushButton{image:url(../image/3.png); border:0px;}
                QPushButton:hover{image:url(../image/3.png); border:4px solid gray;}
            ''')
        self.num_pushButton_3.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_4.setStyleSheet(
            '''
                QPushButton{image:url(../image/4.png); border:0px;}
                QPushButton:hover{image:url(../image/4.png); border:4px solid gray;}
            ''')
        self.num_pushButton_4.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_5.setStyleSheet(
            '''
                QPushButton{image:url(../image/5.png); border:0px;}
                QPushButton:hover{image:url(../image/5.png); border:4px solid gray;}
            ''')
        self.num_pushButton_5.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_6.setStyleSheet(
            '''
                QPushButton{image:url(../image/6.png); border:0px;}
                QPushButton:hover{image:url(../image/6.png); border:4px solid gray;}
            ''')
        self.num_pushButton_6.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_7.setStyleSheet(
            '''
                QPushButton{image:url(../image/7.png); border:0px;}
                QPushButton:hover{image:url(../image/7.png); border:4px solid gray;}
            ''')
        self.num_pushButton_7.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_8.setStyleSheet(
            '''
                QPushButton{image:url(../image/8.png); border:0px;}
                QPushButton:hover{image:url(../image/8.png); border:4px solid gray;}
            ''')
        self.num_pushButton_8.setFont(QtGui.QFont("궁서", 1))
        self.num_pushButton_9.setStyleSheet(
            '''
                QPushButton{image:url(../image/9.png); border:0px;}
                QPushButton:hover{image:url(../image/9.png); border:4px solid gray;}
            ''')
        self.num_pushButton_9.setFont(QtGui.QFont("궁서", 1))
        self.del_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/Del.png); border:0px;}
                QPushButton:hover{image:url(../image/Del.png); border:4px solid gray;}
            ''')
        self.enter_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/확인.png); border-radius:35px;}
                QPushButton:hover{image:url(../image/확인.png); border:4px solid gray;}
            '''
        )
        self.home_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/HOME.png); border:0px; padding: 0px;}
                QPushButton:hover{image:url(../image/HOME.png); border:4px solid gray;}
            '''
        )

        self.password_label.setStyleSheet(
            '''
                 QLabel{image:url(../image/pw_label.png); border:0px;}
            '''
        )

    def sqlConnect(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="apmsetup",
                db="mydb1",
                port=3306,
                charset="utf8"
            )
            print("연결 성공")
            self.cur = self.conn.cursor()
        except:
            print("문제 발생")
            exit(1)


    def closeEvent(self, QCloseEvent):
        print("close")
        self.conn.close()

    def NumClicked(self, state, button):
        exist_line_text = self.q_lineEdit.text()
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()




class KeypadDialog(Keypad, QDialog):
    def __init__(self):
        global carID
        QDialog.__init__(self, None)
        super().__init__()


    def checkAnswer(self):
        try:
            word = str(self.q_lineEdit.text())
            if len(word) >= 4:
                self.cmd = "SELECT password FROM keypad ORDER BY carID"
                self.cur = self.conn.cursor()
                self.cur.execute(self.cmd)
                self.conn.commit()
                ar = self.cur.fetchall()
                self.cmd = "SELECT carID FROM keypad ORDER BY carID"
                self.cur = self.conn.cursor()
                self.cur.execute(self.cmd)
                self.conn.commit()
                ar2 = self.cur.fetchall()

                for i in range(0, 8):
                    if not ar[i][0]:
                        self.cmd = "UPDATE keypad SET password = ('%s') WHERE carID = ('%d')" % (word, ar2[i][0])
                        self.cur = self.conn.cursor()
                        self.cur.execute(self.cmd)
                        self.conn.commit()
                        self.close()
                        save = SaveDialog()
                        save.exec_()

            else:
                tkinter.messagebox.showwarning("경고", "비밀번호가 너무 짧습니다. 4자리 이상 입력해주세요")
        except:
             tkinter.messagebox.showwarning("경고", "동일한 비밀번호가 있습니다. 다시 입력해주세요")



class SaveDialog(QDialog):
    def __init__(self):
        global carID
        QDialog.__init__(self, None)
        uic.loadUi(SaveUI, self)
        i = 0

        self.home_pushButton.clicked.connect(self.home)

        self.home_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/HOME.png); border:0px; padding: 0px;}
                QPushButton:hover{image:url(../image/HOME.png); border:4px solid gray;}
            '''
        )

        self.save_label.setStyleSheet(
            '''
                 QLabel{image:url(../image/saved_label.png); border:0px;}
            '''
        )




    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()


class outDialog(Keypad):
    def __init__(self):
        global carID
        super().__init__()

        self.password_label.setStyleSheet(
            '''
                 QLabel{image:url(../image/pw_label2.png); border:0px;}
            '''
        )
    def checkAnswer(self):
        try:
            self.cmd = "SELECT password FROM keypad ORDER BY carID"
            self.cur.execute(self.cmd)
            self.conn.commit()
            ar = self.cur.fetchall()
            word = str(self.q_lineEdit.text())
            null = ''
            for i in range(0, 7):
                if word in ar[i]:
                    print(ar[i])
                    print(word)
                    self.cmd = "UPDATE keypad SET password = ('%s') WHERE password = ('%s')" % (null, word)
                    self.cur.execute(self.cmd)
                    self.conn.commit()
                    self.close()
                    out = OutcarDialog()
                    out.exec_()
        except:
            tkinter.messagebox.showwarning("경고", "일치하는 비밀번호가 없습니다")







class OutcarDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(OutcarUI, self)
        self.home_pushButton.clicked.connect(self.home)

        self.home_pushButton.setStyleSheet(
            '''
                QPushButton{image:url(../image/HOME.png); border:0px; padding: 0px;}
                QPushButton:hover{image:url(../image/HOME.png); border:4px solid gray;}
            '''
        )

        self.outcar_label.setStyleSheet(
            '''
                 QLabel{image:url(../image/exit_label.png); border:0px;}
            '''
        )

    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainDialog()
    Main.show()
    app.exec_()