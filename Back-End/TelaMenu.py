# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 801, 521))
        self.frame.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButtonMenuVoltar = QtWidgets.QPushButton(self.frame)
        self.pushButtonMenuVoltar.setGeometry(QtCore.QRect(350, 330, 75, 23))
        self.pushButtonMenuVoltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButtonMenuVoltar.setObjectName("pushButtonMenuVoltar")
        self.pushButtonMenuSaque = QtWidgets.QPushButton(self.frame)
        self.pushButtonMenuSaque.setGeometry(QtCore.QRect(270, 150, 241, 28))
        self.pushButtonMenuSaque.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButtonMenuSaque.setObjectName("pushButtonMenuSaque")
        self.pushButtonMenuDeposito = QtWidgets.QPushButton(self.frame)
        self.pushButtonMenuDeposito.setGeometry(QtCore.QRect(270, 110, 241, 28))
        self.pushButtonMenuDeposito.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButtonMenuDeposito.setObjectName("pushButtonMenuDeposito")
        self.pushButtonMenuTransferencia = QtWidgets.QPushButton(self.frame)
        self.pushButtonMenuTransferencia.setGeometry(QtCore.QRect(270, 190, 241, 28))
        self.pushButtonMenuTransferencia.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButtonMenuTransferencia.setObjectName("pushButtonMenuTransferencia")
        self.pushButtonMenuHistorico = QtWidgets.QPushButton(self.frame)
        self.pushButtonMenuHistorico.setGeometry(QtCore.QRect(270, 70, 241, 28))
        self.pushButtonMenuHistorico.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButtonMenuHistorico.setObjectName("pushButtonMenuHistorico")
        self.pushButtonMenuChat = QtWidgets.QPushButton(self.frame)
        self.pushButtonMenuChat.setGeometry(QtCore.QRect(270, 230, 241, 31))
        self.pushButtonMenuChat.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.pushButtonMenuChat.setObjectName("pushButtonMenuChat")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(280, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonMenuVoltar.setText(_translate("MainWindow", "Voltar"))
        self.pushButtonMenuSaque.setText(_translate("MainWindow", "SAQUE"))
        self.pushButtonMenuDeposito.setText(_translate("MainWindow", "DEPOSITO"))
        self.pushButtonMenuTransferencia.setText(_translate("MainWindow", "TRANSFERÊNCIA"))
        self.pushButtonMenuHistorico.setText(_translate("MainWindow", "HISTÓRICO"))
        self.pushButtonMenuChat.setText(_translate("MainWindow", "CHAT"))
        self.label.setText(_translate("MainWindow", "B&V Bank"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
