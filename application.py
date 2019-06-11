#!./venv/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from interface.main_window import Ui_MainWindow
from interface.interviewData_window import Ui_Interview_Data
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

        self.go_to_interview_data()

    def go_to_interview_data(self):
        self.ui = Ui_Interview_Data()
        self.ui.setupUi(self)
        self.ui.pushButton_menu.clicked.connect(self.go_to_main_window)
        self.ui.pushButton_next.clicked.connect(self.next_question)
        self.next_question()

    def next_question(self):
        self.nr_question += 1

        if self.nr_question > len(self.d_tree.feature_names):
            print(self.nr_question, self.interview_data)
            self.go_to_result()
        else:
            if self.nr_question == len(self.d_tree.feature_names):
                self.ui.pushButton_next.setText("Finish")

            if self.nr_question > 0:
                self.interview_data.append(self.ui.doubleSpinBox.value())

            self.ui.doubleSpinBox.setValue(0)
            self.ui.question_label.setText(self.d_tree.feature_names[self.nr_question - 1])
            self.ui.labelNrQuestion.setText(str(self.nr_question) + " of " + str(len(self.d_tree.feature_names)))

    def go_to_result(self):
        if self.classifier:
            result = self.d_tree.predict_by_classification([self.interview_data])
        elif self.regression:
            result = self.d_tree.predict_by_regression([self.interview_data])

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
