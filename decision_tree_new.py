import os
import sklearn
from sklearn import tree
import graphviz
import consts


class MyDecisionTree:

    def __init__(self):
        self.dataset = {'data': [], 'target': []}
        self.clf = tree.DecisionTreeClassifier()

    def load_dataset(self, name):
        list_of_data = []
        with open(name, 'r') as dataset:
            for line in dataset:
                l = [float(x) for x in line.strip().split(',')]
                list_of_data.append(l)

        self.sort_by_target(list_of_data)

        for one_set in list_of_data:
            self.dataset['data'].append(one_set[:-1])
            self.dataset['target'].append(int(one_set[-1]))

    def take_target(self, element):
        return element[consts.NUM]

    def sort_by_target(self, ds):
        ds.sort(key=self.take_target)

    def training(self):
        self.clf = self.clf.fit(self.dataset['data'], self.dataset['target'])
        
    def save_tree(self, name_out_file="out_tree"):
        tree.plot_tree(self.clf)
        dot_data = tree.export_graphviz(self.clf, out_file=None)
        graph = graphviz.Source(dot_data) 
        graph.render("out_tree")


if __name__ == "__main__":
    dc = MyDecisionTree()
    dc.load_dataset(os.path.join('datasets_new', 'new_dataset.data'))
    dc.training()
    dc.save_tree()
