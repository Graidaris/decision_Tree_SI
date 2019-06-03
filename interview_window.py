# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interview_window.ui',
# licensing of 'interview_window.ui' applies.
#
# Created: Wed May 29 09:00:31 2019
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.questionLabel.setFont(font)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout_2.addWidget(self.questionLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.buttonTrue = QtWidgets.QPushButton(self.splitter)
        self.buttonTrue.setObjectName("buttonTrue")
        self.buttonFalse = QtWidgets.QPushButton(self.splitter)
        self.buttonFalse.setObjectName("buttonFalse")
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout.addWidget(self.pushButton_menu)
        spacerItem = QtWidgets.QSpacerItem(599, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_result = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_result.setObjectName("pushButton_result")
        self.horizontalLayout.addWidget(self.pushButton_result)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        QuestionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(QuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(QuestionWindow)
        QuestionWindow.setTabOrder(self.buttonTrue, self.buttonFalse)
        QuestionWindow.setTabOrder(self.buttonFalse, self.pushButton_menu)
        QuestionWindow.setTabOrder(self.pushButton_menu, self.pushButton_result)

    def retranslateUi(self, QuestionWindow):
        QuestionWindow.setWindowTitle(QtWidgets.QApplication.translate("QuestionWindow", "Interview", None, -1))
        self.questionLabel.setText(QtWidgets.QApplication.translate("QuestionWindow", "Question: ", None, -1))
        self.buttonTrue.setText(QtWidgets.QApplication.translate("QuestionWindow", "TRUE", None, -1))
        self.buttonFalse.setText(QtWidgets.QApplication.translate("QuestionWindow", "FALSE", None, -1))
        self.pushButton_menu.setText(QtWidgets.QApplication.translate("QuestionWindow", "Menu", None, -1))
        self.pushButton_result.setText(QtWidgets.QApplication.translate("QuestionWindow", "Show Result", None, -1))

