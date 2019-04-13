# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2nd.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from finalproject import conversation

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 100, 201, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("trainer1.png"))
        self.label_2.setObjectName("label_2")
        self.ladycaption = QtWidgets.QLabel(self.centralwidget)
        self.ladycaption.setGeometry(QtCore.QRect(120, 270, 76, 20))
        self.ladycaption.setObjectName("ladycaption")
        self.coachcaption = QtWidgets.QLabel(self.centralwidget)
        self.coachcaption.setGeometry(QtCore.QRect(450, 270, 76, 20))
        self.coachcaption.setObjectName("coachcaption")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 100, 161, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assistant.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 330, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"background-color: rgb(78, 154, 6);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
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
        self.ladycaption.setText(_translate("MainWindow", "TextLabel"))
        self.coachcaption.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Let\'s have a chit chat!"))
        self.label_4.setText(_translate("MainWindow", "Record/Listen"))

    def setLadyLabel(self, caption):
        _translate = QtCore.QCoreApplication.translate
        self.ladycaption.setText(_translate("MainWindow", caption))

    def setCoachLabel(self, caption):
        _translate = QtCore.QCoreApplication.translate
        self.coachcaption.setText(_translate("MainWindow", caption))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    conversation()

    sys.exit(app.exec_())

