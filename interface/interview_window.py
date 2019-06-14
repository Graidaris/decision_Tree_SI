# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_UI/interview_window.ui',
# licensing of 'interface_UI/interview_window.ui' applies.
#
# Created: Tue Jun 11 13:14:14 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

# Added from me: 
import json
#

class Ui_InterviewWindow(object):    

    def setupUi(self, InterviewWindow):
        InterviewWindow.setObjectName("InterviewWindow")
        InterviewWindow.resize(665, 413)
        self.centralwidget = QtWidgets.QWidget(InterviewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.options_widget_answer = QtWidgets.QWidget(self.centralwidget)
        self.options_widget_answer.setObjectName("options_widget_answer")
        self.verticalLayout_2.addWidget(self.options_widget_answer)
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_buttons.addWidget(self.pushButton_menu)
        spacerItem4 = QtWidgets.QSpacerItem(268, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(spacerItem4)
        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.horizontalLayout_buttons.addWidget(self.pushButton_previous)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(spacerItem5)
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_buttons.addWidget(self.pushButton_next)
        self.verticalLayout_2.addLayout(self.horizontalLayout_buttons)
        InterviewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InterviewWindow)
        QtCore.QMetaObject.connectSlotsByName(InterviewWindow)

    def retranslateUi(self, InterviewWindow):
        InterviewWindow.setWindowTitle(QtWidgets.QApplication.translate("InterviewWindow", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("InterviewWindow", "1 of 13", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("InterviewWindow", "Question", None, -1))
        self.pushButton_menu.setText(QtWidgets.QApplication.translate("InterviewWindow", "Menu", None, -1))
        self.pushButton_previous.setText(QtWidgets.QApplication.translate("InterviewWindow", "Previous", None, -1))
        self.pushButton_next.setText(QtWidgets.QApplication.translate("InterviewWindow", "Next", None, -1))

#Added from me

    # def add_object(self):
    #     self.buttons=[]
    #     for button in range(20):
    #         self.buttons.append(QtWidgets.QPushButton(self.options_widget_answer))
    #         self.buttons[-1].setText(f"hello {button}")
    #         self.buttons[-1].setObjectName(f"hello {button}")        
        
    #     self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.options_widget_answer)
    #     for button in self.buttons:
    #         self.verticalLayout_3.addWidget(button)

    # def delete_objects(self):
    #     for button in self.buttons:
    #         self.verticalLayout_3.removeWidget(button)
    #         button.deleteLater()

    def load_questions_json(self, path):
        with open(path, "r") as questions_json:
            self.questions = json.load(questions_json)

    def next_question(self):
        pass

    def add_question_attributes(self):
        self.added_elements = []
        self.verticalLayout_question_attr = QtWidgets.QVBoxLayout(self.options_widget_answer)
        for name in self.questions:
            self.label.setText(self.questions[name]["question"])
            for field_name in self.questions[name]["field_type"]:
                if field_name == "int":
                    self.add_int_field(self.questions[name]["field_type"][field_name])
                elif field_name == "radio":
                    self.add_radio_field(self.questions[name]["field_type"][field_name])
                elif field_name == "float":
                    self.add_float_field(self.questions[name]["field_type"][field_name])

            for widget in self.added_elements:
                self.verticalLayout_question_attr.addWidget(widget['widget'])

            self.reset_question()


    def add_radio_field(self, attr):        
        for radio in attr:
            radio_button = {
                'widget': QtWidgets.QRadioButton(self.options_widget_answer),
                'value': radio['value']
            }            
            radio_button['widget'].setText(radio['text'])
            self.added_elements.append(radio_button)
            print('added radio')
        
    
    def add_int_field(self, attr):
        spin_box = {
            'widget': QtWidgets.QSpinBox(self.options_widget_answer)
        }
        self.added_elements.append(spin_box)
        print('added int')

    def add_float_field(self, attr):
        double_spin_box = {
            'widget': QtWidgets.QDoubleSpinBox(self.options_widget_answer)
        }
        self.added_elements.append(double_spin_box)
        print('added float')

    def reset_question(self):
        for widget in self.added_elements:
            self.verticalLayout_question_attr.removeWidget(widget['widget'])
            widget['widget'].deleteLater()
