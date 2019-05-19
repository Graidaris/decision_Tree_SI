import os
import sklearn
import consts


class MyDecisionTree:

    def __init__(self):
        self.dataset = {'data': [], 'target': []}

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
        pass


if __name__ == "__main__":
    dc = MyDecisionTree()
    dc.load_dataset(os.path.join('datasets_new', 'new_dataset.data'))
    print(dc.dataset)
