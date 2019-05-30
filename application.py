import sys
import time
import threading
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from interview_window import Ui_QuestionWindow
from main_window import Ui_MainWindow
from interviewData_window import Ui_Interview_Data
from result_window import Ui_ResultMenu



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.go_to_mainWindow()
        
    def go_to_mainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_start.clicked.connect(self.check_preferences)
        
    def check_preferences(self):
        if self.ui.radioButton_classfifier.isChecked():
            print("classfifier")
        elif self.ui.radioButton_regression.isChecked():
            print("regression")
        
        if self.ui.radioButton_quiz.isChecked():
            self.go_to_interview()
        elif self.ui.radioButton_data.isChecked():
            self.go_to_interviewData()
        
    
    def go_to_interview(self):
        self.ui = Ui_QuestionWindow()        
        self.ui.setupUi(self)
        self.ui.buttonTrue.clicked.connect(self.true_next_question)
        self.ui.buttonFalse.clicked.connect(self.false_next_question)
        self.ui.pushButton_result.clicked.connect(self.go_to_result)
        self.ui.pushButton_menu.clicked.connect(self.go_to_mainWindow)
        
    def false_next_question(self):
        print("False next question")
        
    def true_next_question(self):
        print("True next question")
        
    def go_to_interviewData(self):
        self.ui = Ui_Interview_Data()        
        self.ui.setupUi(self)
        self.ui.pushButton_menu.clicked.connect(self.go_to_mainWindow)
        self.ui.pushButton_next.clicked.connect(self.interview_data_next_question)
        
    def interview_data_next_question(self):
        pass
        
    def go_to_result(self):
        self.ui = Ui_ResultMenu()        
        self.ui.setupUi(self)
        self.ui.pushButton_menu.clicked.connect(self.go_to_mainWindow)
        self.ui.pushButton_exit.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())