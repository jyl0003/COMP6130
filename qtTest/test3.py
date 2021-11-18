# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test10.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 831)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectedProject = QtWidgets.QLabel(self.centralwidget)
        self.selectedProject.setGeometry(QtCore.QRect(250, 10, 431, 41))
        self.selectedProject.setObjectName("selectedProject")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 0, 911, 801))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(420, 610, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 191, 801))
        self.widget_2.setObjectName("widget_2")
        self.effectivenessBox = QtWidgets.QComboBox(self.widget_2)
        self.effectivenessBox.setGeometry(QtCore.QRect(20, 80, 161, 31))
        self.effectivenessBox.setObjectName("effectivenessBox")
        self.effectivenessBox.addItem("")
        self.effectivenessBox.addItem("")
        self.privacyBox = QtWidgets.QComboBox(self.widget_2)
        self.privacyBox.setGeometry(QtCore.QRect(20, 210, 161, 31))
        self.privacyBox.setObjectName("privacyBox")
        self.privacyBox.addItem("")
        self.privacyBox.addItem("")
        self.robustnessBox = QtWidgets.QComboBox(self.widget_2)
        self.robustnessBox.setGeometry(QtCore.QRect(20, 400, 161, 31))
        self.robustnessBox.setObjectName("robustnessBox")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.robustnessBox.addItem("")
        self.fairnessBox = QtWidgets.QComboBox(self.widget_2)
        self.fairnessBox.setGeometry(QtCore.QRect(20, 630, 161, 31))
        self.fairnessBox.setObjectName("fairnessBox")
        self.fairnessBox.addItem("")
        self.fairnessBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.effectivenessBox.currentIndexChanged.connect(self.index_changed)
        self.privacyBox.currentIndexChanged.connect(self.index_changed)
        self.robustnessBox.currentTextChanged.connect(self.text_changed)
        self.fairnessBox.currentIndexChanged.connect(self.index_changed)
        
        # self.robustnessBox.activated.connect(self.window2)
        
        self.pushButton.clicked.connect(self.window2)  
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectedProject.setText(_translate("MainWindow", "This will show selected name"))
        self.pushButton.setText(_translate("MainWindow", "open tensorboard"))
        self.effectivenessBox.setItemText(0, _translate("MainWindow", "Effectivness"))
        self.effectivenessBox.setItemText(1, _translate("MainWindow", "Data-Free Knowledge"))
        self.privacyBox.setItemText(0, _translate("MainWindow", "Privacy"))
        self.privacyBox.setItemText(1, _translate("MainWindow", "Inverting Gradients"))
        self.robustnessBox.setItemText(0, _translate("MainWindow", "Robustness"))
        self.robustnessBox.setItemText(1, _translate("MainWindow", "Backdoor Attacks"))
        self.robustnessBox.setItemText(2, _translate("MainWindow", "Data Poisoning Attacks"))
        self.robustnessBox.setItemText(3, _translate("MainWindow", "Model Poisoning Attacks"))
        self.robustnessBox.setItemText(4, _translate("MainWindow", "Byzantine Attacks"))
        self.robustnessBox.setItemText(5, _translate("MainWindow", "Free-rider Attacks"))
        self.robustnessBox.setItemText(6, _translate("MainWindow", "Inference Attacks"))
        self.robustnessBox.setItemText(7, _translate("MainWindow", "Byzantine Robustness"))
        self.robustnessBox.setItemText(8, _translate("MainWindow", "Sybil Robustness"))
        self.robustnessBox.setItemText(9, _translate("MainWindow", "Certified Robustness"))
        self.fairnessBox.setItemText(0, _translate("MainWindow", "Fairness"))
        self.fairnessBox.setItemText(1, _translate("MainWindow", "Fair Averaging"))
        
    def check_index(self, index):
        cindex = self.combobox.currentIndex()
        print(f"Index signal: {index}, currentIndex {cindex}")
        
    def index_changed(self, index):
        self.pushButton1 = QtWidgets.QPushButton(self.widget)
        self.pushButton1.move(275, 200)
        self.pushButton1.setObjectName("testme")
        print("Index changed", index)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def text_changed(self, s):
        if (s == "Backdoor Attacks"):
            print("Text changed:", s)
        
    def window2(self):                                             # <===
        self.web = QWebEngineView()
        self.web.load(QUrl("http://localhost:6006/#scalars"))
        self.web.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
