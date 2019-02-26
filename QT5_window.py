# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 251)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn_Start = QtWidgets.QPushButton(self.centralWidget)
        self.btn_Start.setGeometry(QtCore.QRect(120, 150, 85, 29))
        self.btn_Start.setObjectName("btn_Start")
        self.btn_Stop = QtWidgets.QPushButton(self.centralWidget)
        self.btn_Stop.setGeometry(QtCore.QRect(20, 150, 85, 29))
        self.btn_Stop.setObjectName("btn_Stop")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(120, 127, 89, 17))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 127, 87, 17))
        self.label.setObjectName("label")
        self.btn_Confirmar = QtWidgets.QPushButton(self.centralWidget)
        self.btn_Confirmar.setGeometry(QtCore.QRect(20, 70, 85, 29))
        self.btn_Confirmar.setObjectName("btn_Confirmar")
        self.cbox_Keys = QtWidgets.QComboBox(self.centralWidget)
        self.cbox_Keys.setGeometry(QtCore.QRect(20, 20, 181, 25))
        self.cbox_Keys.setObjectName("cbox_Keys")
        self.cbox_Keys.addItem("")
        self.cbox_Keys.addItem("")
        self.cbox_Keys.addItem("")
        self.cbox_Keys.addItem("")
        self.cbox_Keys.addItem("")
        self.edit_Interval = QtWidgets.QLineEdit(self.centralWidget)
        self.edit_Interval.setGeometry(QtCore.QRect(270, 20, 113, 29))
        self.edit_Interval.setText("")
        self.edit_Interval.setObjectName("edit_Interval")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(390, 20, 51, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 474, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autoclick 0.1"))
        self.btn_Start.setText(_translate("MainWindow", "Start"))
        self.btn_Stop.setText(_translate("MainWindow", "Pause"))
        self.label_2.setText(_translate("MainWindow", " (Ctrl + Shift + S)"))
        self.label.setText(_translate("MainWindow", "(Ctrl + Shift + P)"))
        self.btn_Confirmar.setText(_translate("MainWindow", "Confirm"))
        self.cbox_Keys.setItemText(0, _translate("MainWindow", "LEFT MOUSE BUTTON"))
        self.cbox_Keys.setItemText(1, _translate("MainWindow", "RIGHT MOUSE BUTTON"))
        self.cbox_Keys.setItemText(2, _translate("MainWindow", "KEYBOARD_A"))
        self.cbox_Keys.setItemText(3, _translate("MainWindow", "KEYBOARD_B"))
        self.cbox_Keys.setItemText(4, _translate("MainWindow", "KEYBOARD_C"))
        self.label_3.setText(_translate("MainWindow", "Interval:"))
        self.label_4.setText(_translate("MainWindow", "Seconds"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

