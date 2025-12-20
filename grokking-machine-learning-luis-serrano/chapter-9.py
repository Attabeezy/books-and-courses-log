import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score

dataset = pd.DataFrame({
    'x_0':[7,3,2,1,2,4,1,8,6,7,8,9],
    'x_1':[1,2,3,5,6,7,9,10,5,8,4,6],
    'y':[0,0,0,0,0,0,1,1,1,1,1,1,]
})

features = dataset[['x_0', 'x_1']]
labels = dataset['y']

decision_tree = DecisionTreeClassifier()

decision_tree.fit(X = features, y =labels)

# To train with entropy use criterion
decision_tree = DecisionTreeClassifier(criterion = 'entropy')

data = pd.read_csv('Admission_Predict.csv', index_col = 0)
data['Admitted'] = data['Chance of Admit '] >= 0.75
data = data.drop(['Chance of Admit '], axis=1)

features = data.drop(['Admitted'], axis=1)
labels = data['Admitted']

dt = DecisionTreeClassifier()
dt.fit(X = features, y = labels)

#print(dt.predict(features[0:5]))

# Setting hyperparameters in Sklearn
dt_smaller = DecisionTreeClassifier(max_depth=3,
                                    min_samples_leaf=10, min_samples_split=10)
dt_smaller.fit(X=features, y=labels)

print(dt.predict([[320, 110, 3, 4.0, 3.5, 8.9, 0]]))


# DecisionTree for Regression
features = [[10], [20], [30], [40], [50], [60], [70], [80]]
labels = [7, 5, 7, 1, 2, 1, 5, 4]

dt_regressor = DecisionTreeRegressor(max_depth = 2)
dt_regressor.fit(X = features, y = labels)

print(dt_regressor.predict([[15]]))

"""
Summary
• Decision trees are important machine learning models, used for classification and
regression.
• The way decision trees work is by asking binary questions about our data and making a
prediction based on the answers to those questions.
• The algorithm for building decision trees for classification consists of finding the feature
in our data that best determines the label and iterating over this step.
• We have several ways to tell if a feature determines the label best. The three that we
learned in this chapter are accuracy, Gini impurity index, and entropy.
• The Gini impurity index measures the purity of a set. In that way, a set in which every
element has the same label has a Gini impurity index of 0. A set in which every element
has a different label has a Gini impurity label close to 1.
• Entropy is another measure for the purity of a set. A set in which every element has the
same label has an entropy of 0. A set in which half of the elements have one label and the
other half has another label has an entropy of 1. When building a decision tree, the
difference in entropy before and after a split is called information gain.
• The algorithm for building a decision tree for regression is similar to the one used for
classification. The only difference is that we use the mean square error to select the best
feature to split the data.
• In two dimensions, regression tree plots look like the union of several horizontal lines,
where each horizontal line is the prediction for the elements in a particular leaf.
• Applications of decision trees range very widely, from recommendation algorithms to
applications in medicine and biology.
"""

# Exercise 9.1
# Answer: Spam

# Exercise 9.2
# Data from the Exercise 9.2 table
data = {
    'Transaction': ['Transaction 1', 'Transaction 2', 'Transaction 3', 'Transaction 4', 'Transaction 5', 'Transaction 6'],
    'Value': [100, 100, 10000, 10000, 5000, 100],
    'Approved vendor': [False, True, True, False, True, True],
    'Fraudulent': [True, False, False, True, True, False]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Optional: Drop the 'Transaction' column as it's just an index label
# and convert 'Value' to a more suitable numeric type if needed (though integers are fine here)
df = df.drop(columns=['Transaction'])

X = df[['Value', 'Approved vendor']]
y = df['Fraudulent']

dt_gini = DecisionTreeClassifier(criterion = 'gini')
dt_entropy = DecisionTreeClassifier(criterion = 'entropy')

dt_gini.fit(X, y)
dt_entropy.fit(X, y)

# Exercise 9.3
# Data from the Exercise 9.3 table, using True/False for the 'X' and empty cells
data = {
    'Patient': ['Patient 1', 'Patient 2', 'Patient 3', 'Patient 4', 'Patient 5', 'Patient 6', 'Patient 7', 'Patient 8'],
    'Cough (C)': [False, True, True, True, True, False, False, False],
    'Fever (F)': [True, True, False, True, False, True, True, False],
    'Difficulty breathing (B)': [True, False, True, True, False, True, False, False],
    'Tiredness (T)': [True, True, True, False, True, False, False, True],
    'Diagnosis': [True, True, True, True, False, False, False, False]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Optional: Set 'Patient' as the index, or drop it
df = df.set_index('Patient')

X = df.drop(['Diagnosis'], axis=1)
y = df['Diagnosis']

dt_model = DecisionTreeClassifier(max_depth=1)

dt_model.fit(X, y)

y_pred = dt_model.predict(X)


accuracy = accuracy_score(y, y_pred)

print(accuracy)