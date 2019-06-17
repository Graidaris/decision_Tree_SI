#!./venv/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
from PySide2.QtWidgets import QApplication, QMainWindow
from interface.main_window import Ui_MainWindow
from interface.interview_window import Ui_InterviewWindow
from interface.result_window import Ui_ResultMenu

from decision_tree import DecisionTree


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.nr_question = 0
        self.interview_data = []
        self.classifier = False
        self.regression = False
        self.ui = None
        self.go_to_main_window()
        self.d_tree = DecisionTree()
        path_to_dataset = os.path.join('dataset', 'joint_dataset.data')
        self.d_tree.load_dataset(path_to_dataset)

    def go_to_main_window(self):
        self.reset_data()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(self.check_preferences)

    def reset_data(self):
        self.nr_question = 0
        self.interview_data = []
        self.classifier = False
        self.regression = False

    def check_preferences(self):
        if self.ui.radioButton_classfifier.isChecked():
            self.classifier = True
            self.d_tree.training_classifier()
        elif self.ui.radioButton_regression.isChecked():
            self.regression = True
            self.d_tree.training_regression()

        self.go_to_interview()

    def go_to_interview(self):
        self.ui = Ui_InterviewWindow()        
        self.ui.setupUi(self)
        self.ui.load_questions_json(os.path.join("questions",
                                                 "questions.json"))
        self.ui.pushButton_next.clicked.connect(self.next_question)
        self.ui.pushButton_finish.clicked.connect(self.go_to_result)
        self.ui.pushButton_previous.clicked.connect(self.previous_question)

    def next_question(self):
        self.ui.next_question()

    def previous_question(self):
        self.ui.previous_question()
        
    def go_to_result(self):
        data_to_analysis = self.ui.finish_interview()
        if self.classifier:
            result = self.d_tree.predict_by_classification([data_to_analysis])
        elif self.regression:
            result = self.d_tree.predict_by_regression([data_to_analysis])
            
        self.ui = Ui_ResultMenu()
        self.ui.setupUi(self)
        self.ui.pushButton_menu.clicked.connect(self.go_to_main_window)
        self.ui.pushButton_exit.clicked.connect(self.close)

        self.ui.result_label.setText(str(result))
            


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
