#Project
#Władysław Jakołcewicz
#Katarzyna Pietkiewicz


import numpy as np
import graphviz
from sklearn import tree
import sklearn
import json
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
#import matplotlib.pyplot as plt    #need to fix
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd


features = []

with open("ne_features.data", "r") as dataset:
    for line in dataset:
        line_data = [float(x) for x in line.strip().split(" ")]
        features.append(line_data)


with open("ne_labels.data", "r") as file_of_labels:
    labels = [int(label) for label in file_of_labels.readline().strip().split(" ")]


print(features[10])

#for what need this lines????
x = zip(labels, features)
xs = sorted(x, key=lambda tup: tup[0])
labels = [x[0] for x in xs]
features = [x[1] for x in xs]

features = list(features)
labels = list(labels)
#-------

test_idx = [0, 160, 216, 251, 286]

test_target = []
test_data = []
for id in test_idx:
	test_target.append(labels[id])
	test_data.append(features[id])

clf = tree.DecisionTreeClassifier()
clf.fit(features, labels)


featuresNames = ["age", "sex", "cp", "trestbps", "chol", "fbs",
                 "restecg", "exang", "thalach", "oldpeak", "slope", "ca", "thal"]
classNames = ["zdrowy", "niezdrowy", "niezdrowy", "niezdrowy", "niezdrowy"]

featuresNamesPolish = ["wiek", "płeć", "rodzaj bólu w klatce", "ciśnienie krwi w spoczynku", "cholesterol",
                       "poziom cukru", "wyniki EKG", "duszność", "tętno max", "obniżenie ST", "nachylenie ST", "ca", "talasemia"]

featuresNames = list(featuresNames)
classNames = list(classNames)


def export_pdf_tree():
	dot_data = tree.export_graphviz(clf, out_file=None,
                                 feature_names=featuresNames,
                                 class_names=classNames,
                                 filled=True, rounded=True,
                                 special_characters=True)
	graph = graphviz.Source(dot_data)
	graph.render('tree_d', view=True)


#-----------------
def pca_show():
     pass
# 	x = StandardScaler().fit_transform(features)
# 	pca = PCA(n_components=2)
# 	principalComponents = pca.fit_transform(x)
# 	principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
# 	labelsDF = pd.DataFrame(data = labels, columns = ['target'])
# 	finalDf = pd.concat([principalDf, labelsDF[['target']]], axis=1)
# 	fig = plt.figure(figsize = (8,8))
# 	ax = fig.add_subplot(1,1,1)
# 	ax.set_xlabel(' ', fontsize = 15)
# 	ax.set_ylabel(' ', fontsize = 15)
# 	ax.set_title('2 Component PCA', fontsize = 20)
# 	targets = [0, 1, 2, 3, 4]
# 	colors = ['g', 'b', 'm', 'r', 'k']
# 	for target, color in zip(targets,colors):
# 		indicesToKeep = finalDf['target'] == target
# 		ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
# 					, finalDf.loc[indicesToKeep, 'principal component 2']
# 					, c = color
# 					, s = 50)

# 	tar = ['zdrowy', 'niezdrowy 1', 'niezdrowy 2', 'niezdrowy 3', 'niezdrowy 4']
# 	ax.legend(tar)
# 	ax.grid()
# 	plt.show()
# 	#plt.savefig('plot.png') #save plot in png

# #----------------


def print_tree(t, root=0, depth=1):
    if depth == 1:
        print('def predict(X_i):')
    indent = '    '*depth
    print(indent + '# node %s: impurity = %.2f' %
          (str(root), t.impurity[root]))
    left_child = t.children_left[root]
    right_child = t.children_right[root]

    if left_child == sklearn.tree._tree.TREE_LEAF:
        id = 0
        for num in t.value[root][0]:
            if num > 0.:
                break
            id = id+1
        print(indent + 'return %s # (node %d)' % (classNames[id], root))
    else:
        print(indent + 'if X_i' + str(t.feature[root]) +
              ' < %.2f: # (node %d)' % (t.threshold[root], root))
        print_tree(t, root=left_child, depth=depth+1)

        print(indent + 'else:')
        print_tree(t, root=right_child, depth=depth+1)


def tree_decision(t, values_t, root=0, depth=1):

    left_child = t.children_left[root]
    right_child = t.children_right[root]

    if left_child == sklearn.tree._tree.TREE_LEAF:
        id = -1
        for num in t.value[root][0]:
            id = id+1
            if num > 0:
                break

        return classNames[id]
    else:

        if values_t[t.feature[root]] < t.threshold[root]:
            return tree_decision(t, values_t, root=left_child, depth=depth+1)

        else:
            return tree_decision(t, values_t, root=right_child, depth=depth+1)


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Project SI'
        self.left = 10
        self.top = 50
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        newfont = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
        newfontResult = QtGui.QFont("Times", 12, QtGui.QFont.Bold)

        buttonShowPDF_tree = QPushButton('Print tree pdf', self)
        buttonShowPDF_tree.setFont(newfontResult)
        buttonShowPDF_tree.move(550, 10)
        buttonShowPDF_tree.resize(150, 40)
        buttonShowPDF_tree.clicked.connect(self.pdf_generation_click)

        buttonShowPCA = QPushButton('Show PCA', self)
        buttonShowPCA.setFont(newfontResult)
        buttonShowPCA.move(550, 50)
        buttonShowPCA.resize(150, 40)
        buttonShowPCA.clicked.connect(self.show_pca_click)

        button = QPushButton('Start', self)
        button.setFont(newfont)
        button.move(200, 150)
        button.resize(120, 150)
        button.clicked.connect(self.on_click)

        self.image1 = QPixmap("hh.png")
        self.image2 = QPixmap("bh.png")

        self.labelHeart = QLabel("labelHeart", self)
        self.labelHeart.move(250, 150)
        self.labelHeart.setPixmap(self.image1)

        self.label = QLabel("Data for testing: ", self)
        self.label.move(10, 5)
        self.label.setFont(newfont)
        self.label.setAlignment(Qt.AlignCenter)

        self.labelResult = QLabel("Result ", self)
        self.labelResult.move(200, 300)
        self.labelResult.resize(200, 100)
        self.labelResult.setFont(newfontResult)

        self.labelTests = QLabel("labelTests", self)
        self.labelTests.move(10, 50)

        text = ""
        for line in test_data:
            text += str(line) + '\n'

        self.labelTests.setText(text)

        self.labelTestsResult = QLabel("labelTestsResult", self)
        self.labelTestsResult.move(380, 50)
        text = ""
        for test in test_data:
            text += tree_decision(clf.tree_, test) + '\n'

        self.labelTestsResult.setText(text)

        self.labelFeaturesNames = QLabel("labelFeaturesNames", self)
        self.labelFeaturesNames.move(10, 150)
        text = ""
        i = 0
        for line in featuresNamesPolish:
            i += 1
            text += str(i) + ') ' + line + '\n\n'

        self.labelFeaturesNames.setText(text)

        size = 25

        self.textbox = []
        for id in range(13):
            self.textbox.append(QLineEdit(self))
            self.textbox[id].move(150, 150 + size * id)
            self.textbox[id].resize(50, 25)
            self.textbox[id].setText("0")

        self.show()

    @pyqtSlot()
    def on_click(self):
        array = []
        for id in range(13):
            array.append(float(self.textbox[id].text()))
        result = tree_decision(clf.tree_, array)
        self.labelResult.setText(result)
        if result == "niezdrowy":
            self.labelHeart.setPixmap(self.image2)
        else:
            self.labelHeart.setPixmap(self.image1)

    @pyqtSlot()
    def pdf_generation_click(self):
        export_pdf_tree()

    @pyqtSlot()
    def show_pca_click(self):
        pca_show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
