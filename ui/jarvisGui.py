# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\jarvisGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# converted by "pyuic5 -o ui_form.py jarvisGui.ui"
# type "designer"


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1400, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\VIKASH\Desktop\Python\JarvisProject\images/7LP8.gif"))
        self.label.setObjectName("label")

        # Output screen
        # self.groupBox_2 = QtWidgets.QGroupBox("groupBox_2", self.centralwidget)
        # self.output_rd = QtWidgets.QTextBrowser(self.groupBox_2)
        # self.output_rd.setGeometry(QtCore.QRect(10, 90, 331, 111))
        # self.output_rd.setObjectName("output_rd")

#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(1110, 810, 85, 40))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton.setFont(font)
#         self.pushButton.setStyleSheet("background-color: rgb(85, 0, 0);\n"
# "color: rgb(255, 255, 255);\n"
# "border-color: rgb(0, 0, 0);")
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(1199, 810, 85, 40))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton_2.setFont(font)
#         self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
# "border-color: rgb(0, 0, 0);\n"
# "background-color: rgb(170, 0, 0);")
#         self.pushButton_2.setObjectName("pushButton_2")

        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(50, 530, 351, 211))
        # self.label_2.setText("")
        # self.label_2.setPixmap(QtGui.QPixmap(r"C:\Users\VIKASH\Desktop\Python\JarvisProject\images/jarvis.gif"))
        # self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(750, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
"border-radius: none;\n"
"color: white;\n"
"font-size: 20px")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1070, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
"border-radius: none;\n"
"color: white;\n"
"font-size: 20px")
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis"))

        # self.pushButton.setText(_translate("MainWindow", "Run"))
        # self.pushButton_2.setText(_translate("MainWindow", "Exit"))
    def output(self):
        #     self.output_rd.append(str(rad_dis))
            self.output_rd.append("Hello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
