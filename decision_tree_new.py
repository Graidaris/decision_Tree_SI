import os
import sklearn
from sklearn import tree
import graphviz
import consts


class MyDecisionTree:

    feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
                     'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    target_names = ['No presence', 'Presence 1',
                    'Presence 2', 'Presence 3', 'Presence 4']

    def __init__(self):
        self.dataset = {'data': [], 'target': []}
        self.tree_classifier = tree.DecisionTreeClassifier()
        self.tree_regressor = tree.DecisionTreeRegressor()

    def load_dataset(self, name):
        list_of_data = []
        with open(name, 'r') as dataset:
            for line in dataset:
                l = [float(x) for x in line.strip().split(',')]
                list_of_data.append(l)

        self.__sort_by_target(list_of_data)

        for one_set in list_of_data:
            self.dataset['data'].append(one_set[:-1])
            self.dataset['target'].append(int(one_set[-1]))

    def __take_target(self, element):
        return element[consts.NUM]

    def __sort_by_target(self, ds):
        ds.sort(key=self.__take_target)

    def training_to_classifier(self):
        self.tree_classifier = self.tree_classifier.fit(
            self.dataset['data'], self.dataset['target'])

    def training_to_regression(self):
        targets_for_regression = [float(x) for x in self.dataset['target']]
        self.tree_regressor = self.tree_regressor.fit(
            self.dataset['data'], targets_for_regression)
        
    def regression_predict(self, data):
        return self.tree_regressor.predict(data)
    
    def classification_predict(self, data):
        return self.tree_classifier.predict_proba(data, [1.0]*13)

    def save_tree_classifier(self, name_out_file="out_tree"):
        tree.plot_tree(self.tree_classifier)
        dot_data = tree.export_graphviz(self.tree_classifier, out_file=None,
                                        feature_names=self.feature_names,
                                        class_names=self.target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)
        graph.render(name_out_file)


if __name__ == "__main__":
    dc = MyDecisionTree()
    dc.load_dataset(os.path.join('datasets_new', 'new_dataset.data'))
    dc.training_to_classifier()
    dc.training_to_regression()  
    print(dc.classification_predict([23.0, 1.0, 4.0, 160.0, 165.0, 0.0, 0.0, 150.0, 0.0, 2.3, 2.0, 0.0, 3.0]))
