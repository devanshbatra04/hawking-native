# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 171, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("hawking-logo.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 120, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 450, 201, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 211, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("teacher.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 190, 151, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("brain.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(280, 330, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 380, 191, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 450, 191, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 190, 131, 131))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("depression.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 340, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 380, 161, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(570, 450, 100, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(29, 380, 201, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 25))
        self.menubar.setObjectName("menubar")
        self.menuHawking = QtWidgets.QMenu(self.menubar)
        self.menuHawking.setObjectName("menuHawking")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHawking.addSeparator()
        self.menuHawking.addSeparator()
        self.menubar.addAction(self.menuHawking.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Your gateway to freedom!"))
        self.pushButton.setText(_translate("MainWindow", "Check for Autism"))
        self.pushButton.clicked.connect(self.openTests)
        self.label_3.setText(_translate("MainWindow", "Not sure if this app is for you?"))
        self.label_5.setText(_translate("MainWindow", "Have a nice chit chat? We have your back and we don\'t judge either :-)"))
        self.label_7.setText(_translate("MainWindow", "Check for parkinson\'s disease "))
        self.pushButton_3.setText(_translate("MainWindow", "Coin Collection Game"))
        self.pushButton_3.clicked.connect(self.openCoinCollect)
        self.pushButton_4.setText(_translate("MainWindow", "Mouse Game Exercise"))
        self.pushButton_4.clicked.connect(self.openMouseGame)
        self.label_9.setText(_translate("MainWindow", "Why? What if? No , I can\'t!"))
        self.pushButton_5.setText(_translate("MainWindow", "Feeling Depressed?"))
        self.pushButton_5.clicked.connect(self.openTests)
        self.pushButton_6.setText(_translate("MainWindow", "Let\'s Talk"))
        self.pushButton_6.clicked.connect(self.openChat)
        self.pushButton_2.setText(_translate("MainWindow", "Start a healthy Convo"))
        self.pushButton_2.clicked.connect(self.clickConvo)
        self.menuHawking.setTitle(_translate("MainWindow", "Haw&king"))

    def clickConvo(self):
        import os
        os.system('cd conversation && python3 ' + 'conversation.py' + ' & disown')

    def openTests(self):
        import os
        os.system('python3 ' + 'result.py' + ' & disown')

    def openCoinCollect(self):
        import webbrowser
        webbrowser.open_new("http://localhost:3000/handtrack")

    def openMouseGame(self):
        import webbrowser
        webbrowser.open_new("http://localhost:3000/mouse")

    def openChat(self):
        import webbrowser
        webbrowser.open_new("http://localhost:3000/chat")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

