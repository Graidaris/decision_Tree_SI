# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interviewData_window.ui',
# licensing of 'interviewData_window.ui' applies.
#
# Created: Wed May 29 09:01:48 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Interview_Data(object):
    def setupUi(self, Interview_Data):
        Interview_Data.setObjectName("Interview_Data")
        Interview_Data.resize(579, 393)
        self.centralwidget = QtWidgets.QWidget(Interview_Data)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelNrQuestion = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.labelNrQuestion.setFont(font)
        self.labelNrQuestion.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.labelNrQuestion.setObjectName("labelNrQuestion")
        self.horizontalLayout.addWidget(self.labelNrQuestion)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.questionTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.questionTextBrowser.setOverwriteMode(True)
        self.questionTextBrowser.setTabStopWidth(200)
        self.questionTextBrowser.setTabStopDistance(200.0)
        self.questionTextBrowser.setOpenExternalLinks(False)
        self.questionTextBrowser.setObjectName("questionTextBrowser")
        self.horizontalLayout_2.addWidget(self.questionTextBrowser)
        spacerItem3 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(900.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_3.addWidget(self.pushButton_menu)
        spacerItem4 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_3.addWidget(self.pushButton_next)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        Interview_Data.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interview_Data)
        QtCore.QMetaObject.connectSlotsByName(Interview_Data)

    def retranslateUi(self, Interview_Data):
        Interview_Data.setWindowTitle(QtWidgets.QApplication.translate("Interview_Data", "MainWindow", None, -1))
        self.labelNrQuestion.setText(QtWidgets.QApplication.translate("Interview_Data", "1 of 10", None, -1))
        self.questionTextBrowser.setHtml(QtWidgets.QApplication.translate("Interview_Data", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Question</span></p></body></html>", None, -1))
        self.pushButton_menu.setText(QtWidgets.QApplication.translate("Interview_Data", "Menu", None, -1))
        self.pushButton_next.setText(QtWidgets.QApplication.translate("Interview_Data", "Next", None, -1))

