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
        try:
            with open(name, 'r') as dataset:
                for line in dataset:
                    l = [float(x) for x in line.strip().split(',')]
                    list_of_data.append(l)
        except FileNotFoundError:
            print(f"ERROR: File {name} not found")
            return None
        except Exception as e:
            print(f"ERROR with open file {name} - {e}")
            return None

        self.__sort_by_target(list_of_data)

        for one_set in list_of_data:
            self.dataset['data'].append(one_set[:-1])
            self.dataset['target'].append(int(one_set[-1]))

    def __take_target(self, element):
        return element[consts.NUM]

    def __sort_by_target(self, ds):
        ds.sort(key=self.__take_target)

    def training_classifier(self):
        self.tree_classifier = self.tree_classifier.fit(
            self.dataset['data'], self.dataset['target'])

    def training_regression(self):
        targets_for_regression = [float(x) for x in self.dataset['target']]
        self.tree_regressor = self.tree_regressor.fit(
            self.dataset['data'], targets_for_regression)

    def predict_class(self, array):
        """ Predict the class, using sklearn library classification.predict """

        return self.tree_classifier.predict(array)

    def predict_reg(self, array):
        """ Predict the class by regression, using sklearn library regression.predict """

        return self.tree_regressor.predict(array)

    def save_tree(self, name_out_file="tree_of_classification"):
        """ 
        Save the tree of classification 
        Will be saved two files:
        First file have pdf format
        Second without any format, just file contains data of the tree 
        
        Important: for use it is necessary to train the classifier.
        """

        tree.plot_tree(self.tree_classifier)
        dot_data = tree.export_graphviz(self.tree_classifier, out_file=None,
                                        feature_names=self.feature_names,
                                        class_names=self.target_names,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = graphviz.Source(dot_data)
        graph.render(name_out_file)


if __name__ == "__main__":
    """ Some commands to test """

    dc = MyDecisionTree()
    dc.load_dataset(os.path.join('datasets_new', 'new_dataset.data'))
    dc.training_classifier()
    dc.training_regression()
    print(dc.predict_by_classification(
        [[54.0, 1.0, 4.0, 130.0, 239.0, 0.0, 0.0, 155.0, 0.0, 1.2, 1.0, 0.0, 3.0]]))
    print(dc.predict_by_regression(
        [[54.0, 1.0, 4.0, 150.0, 239.0, 0.0, 0.0, 165.0, 0.0, 1.2, 1.0, 0.0, 3.0]]))
