# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyaudio, wave
from Autism.AutismCheck import predict as predictAutism
from Depression.DepressionCheck import predict as predictDepression
from Parkinson.ParkinsonCheck import predict as predictParkinson

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, -10, 151, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("record.png"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 270, 100, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 270, 100, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 270, 131, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 190, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 140, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 340, 471, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 370, 461, 21))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.record_file(10)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Autism Test"))
        self.pushButton_2.clicked.connect(self.getAutismTest)
        self.pushButton_3.setText(_translate("MainWindow", "Depression"))
        self.pushButton_3.clicked.connect(self.getDepressionTest)
        self.pushButton_4.setText(_translate("MainWindow", "Parkinson Test"))
        self.pushButton_4.clicked.connect(self.getParkinsonTest)

        self.label_2.setText(_translate("MainWindow", "CHECK RESULTS"))
        self.label_3.setText(_translate("MainWindow", "Recording..."))
        self.label_4.setText(_translate("MainWindow", "Results:"))

    def record_file(self, time):
        language_code = 'en-US'  # a BCP-47 language tag
        words = []
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = time
        WAVE_OUTPUT_FILENAME = "voice-results.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        wf.writeframes(b''.join(frames))
        wf.close()
        return WAVE_OUTPUT_FILENAME

    def getAutismTest(self):
        _translate = QtCore.QCoreApplication.translate
        result = predictAutism("voice-results.wav")
        if result[0] == 0:
            self.label_5.setText(_translate("Main Window", "Congratulations, you are not Autistic!"))
        else:
            self.label_5.setText(_translate("Main Window", "You may be Autistic, meet a doctor today!"))

    def getDepressionTest(self):
        _translate = QtCore.QCoreApplication.translate
        result = predictDepression("voice-results.wav")
        if result[0] == 0:
            self.label_5.setText(_translate("Main Window", "Congratulations, you are not Depressed!"))
        else:
            self.label_5.setText(_translate("Main Window", "You may be depressed, it's better to talk to someone"))

    def getParkinsonTest(self):
        _translate = QtCore.QCoreApplication.translate
        result = predictDepression("voice-results.wav")
        if result[0] == 0:
            self.label_5.setText(_translate("Main Window", "Congratulations, you are free of Parkinson!"))
        else:
            self.label_5.setText(_translate("Main Window", "You may have Parkinson's disease, please take care."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

