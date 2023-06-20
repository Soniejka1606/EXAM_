# -*- coding: utf-8 -*-
from functools import partial

# Form implementation generated from reading ui file 'autirize.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QMessageBox

import main_qt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 425)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 40, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white;")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 120, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 61, 31))

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_2.setStyleSheet("color: white;")


        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: white;")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 280, 251, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        pixmap = QtGui.QPixmap("pic_qt/backdr.jpg")
        background_label = QtWidgets.QLabel(Dialog)
        background_label.setGeometry(Dialog.rect())
        background_label.setPixmap(pixmap.scaled(Dialog.size()))  # Масштабируем изображение под размер виджета
        background_label.lower()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "АВТОРИЗАЦИЯ"))
        self.label_2.setText(_translate("Dialog", "Логин:"))
        self.label_3.setText(_translate("Dialog", "Пароль:"))
        self.pushButton_3.setText(_translate("Dialog", "Войти"))
        self.pushButton_3.clicked.connect(partial(self.auto, Dialog))


    def auto(self,Dialog):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if login == "" or password == "":
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Нужно заполнить все поля")
            message_box.setWindowTitle("Error ошибка ввода")
            message_box.exec()
            return 0
        if login!="Admin" or password !="Admin":
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setText("Неверный логин или пароль")
            message_box.setWindowTitle("Error неправильные данные")
            message_box.exec()
            return 0
        if login =="Admin" or password == "Admin":
            Dialog.close()
            Dialog = QtWidgets.QDialog()
            ui1 = main_qt.Ui_Dialog()
            ui1.setupUi(Dialog)
            Dialog.show()
            Dialog.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
