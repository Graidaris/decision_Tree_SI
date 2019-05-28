# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interview_window.ui',
# licensing of 'interview_window.ui' applies.
#
# Created: Tue May 28 14:01:18 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_QuestionWindow(object):
    def setupUi(self, QuestionWindow):
        QuestionWindow.setObjectName("QuestionWindow")
        QuestionWindow.resize(712, 457)
        self.centralwidget = QtWidgets.QWidget(QuestionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(4)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        QuestionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QuestionWindow)
        self.statusbar.setObjectName("statusbar")
        QuestionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(QuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(QuestionWindow)

    def retranslateUi(self, QuestionWindow):
        QuestionWindow.setWindowTitle(QtWidgets.QApplication.translate("QuestionWindow", "Interview", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("QuestionWindow", "Question: ", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("QuestionWindow", "TRUE", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("QuestionWindow", "FALSE", None, -1))

