# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interviewData_window.ui',
# licensing of 'interviewData_window.ui' applies.
#
# Created: Sun Jun  2 18:35:50 2019
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
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
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.question_label = QtWidgets.QLabel(self.centralwidget)
        self.question_label.setObjectName("question_label")
        self.horizontalLayout_2.addWidget(self.question_label)
        spacerItem4 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(900.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_2.addWidget(self.doubleSpinBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_3.addWidget(self.pushButton_menu)
        spacerItem6 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_3.addWidget(self.pushButton_next)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        Interview_Data.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interview_Data)
        QtCore.QMetaObject.connectSlotsByName(Interview_Data)

    def retranslateUi(self, Interview_Data):
        Interview_Data.setWindowTitle(QtWidgets.QApplication.translate("Interview_Data", "MainWindow", None, -1))
        self.labelNrQuestion.setText(QtWidgets.QApplication.translate("Interview_Data", "1 of 10", None, -1))
        self.question_label.setText(QtWidgets.QApplication.translate("Interview_Data", "TextLabel", None, -1))
        self.pushButton_menu.setText(QtWidgets.QApplication.translate("Interview_Data", "Menu", None, -1))
        self.pushButton_next.setText(QtWidgets.QApplication.translate("Interview_Data", "Next", None, -1))

