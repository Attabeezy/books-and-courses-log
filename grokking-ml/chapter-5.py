import random
import numpy as np


# Summary
# • Classification is an important part of machine learning. It is similar to regression in that
# it consists of training an algorithm with labeled data and using it to make predictions on
# future (unlabeled) data. The difference from regression is that in classification, the
# predictions are categories, such as yes/no, spam/ham, and so on.
# • Perceptron classifiers work by assigning a weight to each of the features and a bias. The
# score of a data point is calculated as the sum of products of the weights and features, plus
# the bias. If the score is greater than or equal to zero, the classifier predicts a yes.
# Otherwise, it predicts a no.
# • For sentiment analysis, a perceptron consists of a score for each of the words in the
# dictionary, together with a bias. Happy words normally end up with a positive score, and
# sad words with a negative score. Neutral words such as the likely end up with a score close
# to zero.
# • The bias helps us decide if the empty sentence is happy or sad. If the bias is positive, then
# the empty sentence is happy, and if it is negative, then the empty sentence is sad.
# • Graphically, we can see a perceptron as a line trying to separate two classes of points,
# which can be seen as points of two different colors. In higher dimensions, a perceptron is
# a hyperplane separating points.
# • The perceptron algorithm works by starting with a random line and then slowly moving
# it to separate the points well. In every iteration, it picks a random point. If the point is
# correctly classified, the line doesn’t move. If it is misclassified, then the line moves a little
# bit closer to the point to pass over it and classify it correctly.
# • The perceptron algorithm has numerous applications, including spam email detection,
# recommendation systems, e-commerce, and health care.
#
#
# features = np.array([[1,0],[0,2],[1,1],[1,2],[1,3],[2,2],[2,3],[3,2]])
# labels = np.array([0,0,0,0,1,1,1,1])

# THE PERCEPTRON ALGORITHM
def score(weights, bias, features):
    return np.dot(features, weights) + bias

def step(x):
    if x >= 0:
        return 1
    else:
        return 0

def prediction(weights, bias, features):
    return step(score(weights, bias, features))

def error(weights, bias, features, label):
    pred = prediction(weights, bias, features)
    if pred == label:
        return 0
    else:
        return np.abs(score(weights, bias, features))

def mean_perceptron_error(weights, bias, features, labels):
    total_error = 0
    for i in range(len(features)):
        total_error += error(weights, bias, features[i], labels[i])
    return total_error / len(features)

def perceptron_trick(weights, bias, features, label, learning_rate = 0.01):
    pred = prediction(weights, bias, features)
    for i in range(len(weights)):
        weights[i] += learning_rate * (label - pred) * features[i]
    bias += learning_rate * (label - pred)
    return weights, bias

def perceptron_algorithm(features, labels, learning_rate = 0.01, epochs = 200):
    weights = [1.0 for i in range(len(features[0]))]
    bias = 0.0
    errors = []
    for epoch in range(epochs):
        error = mean_perceptron_error(weights, bias, features, labels)
        errors.append(error)
        i = random.randint(0, len(features) - 1)
        weights, bias = perceptron_trick(weights, bias, features[i], labels[i], learning_rate=learning_rate)
        return weights, bias, errors

# print(perceptron_algorithm(features, labels))


# Exercise 5.1: Perceptron Implementation for given data

import pandas as pd

# Data represented as a list of dictionaries with all values as 1s and 0s.
# Key Mapping:
# C: Cough, F: Fever, B: Difficulty breathing, T: Tiredness
# D: Diagnosis (1 = Sick, 0 = Healthy)
data = [
    {'C': 0, 'F': 1, 'B': 1, 'T': 1, 'D': 1}, # Patient 1: Sick
    {'C': 1, 'F': 1, 'B': 0, 'T': 1, 'D': 1}, # Patient 2: Sick
    {'C': 1, 'F': 0, 'B': 1, 'T': 1, 'D': 1}, # Patient 3: Sick
    {'C': 1, 'F': 1, 'B': 1, 'T': 0, 'D': 1}, # Patient 4: Sick
    {'C': 1, 'F': 0, 'B': 0, 'T': 1, 'D': 0}, # Patient 5: Healthy
    {'C': 0, 'F': 1, 'B': 1, 'T': 0, 'D': 0}, # Patient 6: Healthy
    {'C': 0, 'F': 1, 'B': 0, 'T': 0, 'D': 0}, # Patient 7: Healthy
    {'C': 0, 'F': 0, 'B': 0, 'T': 1, 'D': 0}, # Patient 8: Healthy
]

# Create the DataFrame directly from the list of dictionaries
df = pd.DataFrame(data)

# Optional: Rename columns to full names for clarity while keeping the 1/0 data
df.rename(columns={
    'C': 'Cough',
    'F': 'Fever',
    'B': 'Difficulty breathing',
    'T': 'Tiredness',
    'D': 'Diagnosis'
}, inplace=True)

# Display the resulting DataFrame
print(df)

weights, bias, errors = perceptron_algorithm(df[['Cough', 'Fever', 'Difficulty breathing', 'Tiredness']].to_numpy(),
                     df['Diagnosis'].to_numpy(),
                     learning_rate=0.1,
                     epochs=1000)


print("Weights:", weights)
print("Bias:", bias)
print("Errors:", errors)



# Exercise 5.2

# given the point (x1, x2) has the prediction y = step(2x1 + 3x2 -4),
# and the model has boundary line 2x1 _ 3x2 -4 = 0,
# we have p =(1,1) with label y=0

# verify that p is misclassified

def model(x1, x2):
    return step((2 * x1) + (3 * x2) - 4)

print("Prediction for point (1,1):", model(1, 1), "\nShould be 0")  # should be 0

# yes, misclassified

# b. calculate perceptron error that model produces at point p

weights_np = np.array([2.0, 3.0])
features_np = np.array([[1.0, 1.0]])  # shape (1, 2)
labels_np = np.array([0])             # shape (1,)

pError = mean_perceptron_error(weights_np, -4.0, features_np, labels_np)
print("Perceptron Error at point (1,1):", pError)

# c. apply perceptron trick to update the boundary line to still misclassify point p but reduce error, use learning rate 0.01


new_weights, new_bias = perceptron_trick(weights_np, -4.0, features_np[0], labels_np[0], learning_rate=0.01)
print("Updated weights:", new_weights)
print("Updated bias:", new_bias)
new_pError = mean_perceptron_error(new_weights, new_bias, features_np, labels_np)
print("New Perceptron Error at point (1,1):", new_pError)

# d. find new prediction given new model for point p
new_prediction = prediction(new_weights, new_bias, features_np[0])
print("New prediction for point (1,1):", new_prediction)
new_pError = mean_perceptron_error(new_weights, new_bias, features_np, labels_np)
print("New Perceptron Error at point (1,1):", new_pError)


# Exercise 5.3: Using Perceptrons for building logical gates AND and OR
x = np.array([[0,0],[0,1],[1,0],[1,1]])

# a. AND gate
y = np.array([0,0,0,1])  # AND gate labels

def AND_gate():
    weights, bias, errors = perceptron_algorithm(x, y, learning_rate=0.1, epochs=100)
    return weights, bias, errors

print("AND gate weights and bias:", AND_gate())

# b. OR gate
y = np.array([0,1,1,1])  # OR gate labels

def OR_gate():
    weights, bias, errors = perceptron_algorithm(x, y, learning_rate=0.1, epochs=100)
    return weights, bias, errors

print("OR gate weights and bias:", OR_gate())

# c. Explain why a single perceptron cannot be used to build a XOR gate.
"""_summary_
A single perceptron cannot be used to build a XOR gate because the XOR function is not linearly separable.
This means that there is no straight line (or hyperplane in higher dimensions) that can separate
the input space into two regions corresponding to the two classes of the XOR function.
As a result, a single-layer perceptron, which can only learn linear decision boundaries, cannot correctly classify the XOR inputs."""

y = np.array([0,1,1,0])  # XOR gate labels

def XOR_gate():
    weights, bias, errors = perceptron_algorithm(x, y, learning_rate=0.1, epochs=100)
    return weights, bias, errors

print("XOR gate weights and bias (should give us a large error):", XOR_gate())