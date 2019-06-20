# -*- coding: utf-8 -*-
import os

from decision_tree import DecisionTree
import matplotlib.pyplot as plt
import pandas as pd

path_to_dataset = os.path.join('dataset', 'joint_dataset.data')

with open(path_to_dataset, 'r') as f:
    dataset = [[float(a) for a in line.split(',')] for line in f.read().split('\n') if line is not '']
    
    
test_dataset = dataset[(len(dataset)//2):]
dataset = dataset[:(len(dataset)//2)]

results_classifier = []
results_regressor = []
depths = []

for i in range(20):
    d_tree = DecisionTree(max_depth=(i+1))
    d_tree.load_to_datset(dataset)
    
    d_tree.training_classifier()
    d_tree.training_regression()
    
    true_classifier = 0
    false_classifier = 0
    
    true_regressor = 0
    false_regressor = 0
    
    for test_data in test_dataset:
        predict_class = d_tree.predict_by_classification([test_data[:-1]])[0]
        predict_regres = d_tree.predict_by_regression([test_data[:-1]])[0]
        correct = int(test_data[-1])
        
        if predict_class == correct:
            true_classifier += 1
        else:
            false_classifier += 1
            
        if predict_regres == correct:
            true_regressor += 1
        else:
            false_regressor += 1  
            
    true_per = true_classifier/(true_classifier + false_classifier) * 100
    results_classifier.append(true_per)
    
    true_per = true_regressor/(true_regressor + false_regressor) * 100
    results_regressor.append(true_per)
    depths.append(i+1)
    
    
    
    
folder_name = 'pictures'
name_png = 'predict.png'
new_name = name_png

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

count = 0
while True:
    path_to_picture = os.path.join(folder_name,new_name)
    if os.path.exists(path_to_picture):
        count += 1
        new_name = name_png.split('.')
        new_name = str(new_name[0] + str(count) + '.' + new_name[1])
    else:
        break
    
    
    
df = pd.DataFrame(
    {
        'classifier_predict':results_classifier,
        'regressor_predict':results_regressor,
        'depth_of_tree':depths
    }
)
    
ax = plt.gca()
df.plot(kind='line',x='depth_of_tree',y='classifier_predict',ax=ax)
df.plot(kind='line',x='depth_of_tree',y='regressor_predict', color='red' ,ax=ax)



plt.savefig(path_to_picture)
