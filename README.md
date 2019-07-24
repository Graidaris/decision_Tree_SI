# Heart disease detector
The project aims to detect the presence of heart disease in patients based on medical data using the decision tree algorithm (scikit-learn).

# Data used

All the datasets I downloaded are taken from: [http://archive.ics.uci.edu](http://archive.ics.uci.edu/ml/datasets/heart+Disease)

Used datasets:
- processed.hungarian.data
- processed.cleveland.data
- processed.hungarian.data
- processed.switzerland.data
- processed.va.data

# Analysis
Percent of predict is about 56% when the depth of the tree is 6.</br>
Based on tests, classification predictions work better than regression.
![graph](https://github.com/Graidaris/heart_disease_detector/blob/master/pictures/predict.png)

# Getting started
1. Install python 3.7.*
2. Install all important dependencies:
   - ```pip install -r requirement.txt```
3. Start the program:
   - ``` python3 application.py ```
