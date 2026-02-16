"""
Summary
• Continuous perceptrons, or logistic classifiers, are similar to perceptron classifiers,
except instead of making a discrete prediction such as 0 or 1, they predict any number
between 0 and 1.
• Logistic classifiers are more useful than discrete perceptrons, because they give us more
information. Aside from telling us which class the classifier predicts, they also give us a
probability. A good logistic classifier would assign low probabilities to points with label 0
and high probabilities to points with label 1.
• The log loss is an error function for logistic classifiers. It is calculated separately for every
point as the negative of the natural logarithm of the probability that the classifier assigns
to its label.
• The total log loss of a classifier on a dataset is the sum of the log loss at every point.
• The logistic trick takes a labeled data point and a boundary line. If the point is
incorrectly classified, the line is moved closer to the point, and if it is correctly classified,
the line is moved farther from the point. This is more useful than the perceptron trick,
because the perceptron trick does not move the line if the point is correctly classified.
• The logistic regression algorithm is used to fit a logistic classifier to a labeled dataset. It
consists of starting with a logistic classifier with random weights and continuously
picking a random point and applying the logistic trick to obtain a slightly better
classifier.
• When we have several classes to predict, we can build several linear classifiers and
combine them using the softmax function.
"""

# Implementation of Logistic Regression from scratch
from random import random
import numpy as np
from sklearn import utils

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def score(weights, bias, features):
    return np.dot(weights, features) + bias

def prediction(weights, bias, features):
    return sigmoid((score(weights, bias, features)))

def log_loss(weights, bias, features, label):
    pred = prediction(weights, bias, features)
    return - (label * np.log(pred) + (1 - label) * np.log(1 - pred))

def total_log_loss(weights, bias, features, labels):
    total_error = 0
    for i in range(len(labels)):
        total_error += log_loss(weights, bias, features[i], labels[i])
    return total_error

def logistic_regression_trick(weights, bias, features, label, learning_rate=0.01, epoch=1000):
    for _ in range(epoch):
        pred = prediction(weights, bias, features)
        error = pred - label
        for i in range(len(weights)):
            weights[i] += (label - pred) * features[i] * learning_rate
            bias += (label - pred) * learning_rate
    return weights, bias

def logistic_regression_algorithm(features, labels, learning_rate = 0.01, epochs = 1000):
    utils.plot_points(features, labels)
    weights = [1.0 for i in range(len(features[0]))]
    bias = 0.0
    errors = []
    for i in range(epochs):
        errors.append(total_log_loss(weights, bias, features, labels))
        j = random.randint(0, len(labels) - 1)
        weights, bias = logistic_regression_trick(weights, bias, features[j], labels[j], learning_rate)
    return weights, bias, errors

def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / exp_z.sum(axis=0)

# Exercise 6.1: implement prediction for given data
# given sigmoid(d + 0.5c - 0.8), what is the prediction for c=1 and d=1?

weights = [1, 0.5] # d + 0.5c
bias = -0.8
features = [1, 1]  # c=1, d=1

pred = prediction(weights, bias, features)
#print("Prediction for c=1 and d=1:", pred)

# Exercise 6.2: implement logistic regression for given data
# given sigmoid(2x1 + 3x2 -4), p = (1, 1), label = 0, calculate prediction and log loss

# predition calculation
weights = [2, 3]  # 2x1 + 3x2
bias = -4
features = [1, 1]  # x1=1, x2=1

#print("Prediction for p: ", prediction(weights, bias, features))

# log loss calculation
label = 0

#print("Log Loss for p: ", log_loss(weights, bias, features, label))

# use logistic trck to obtain a new model that producess smaller log loss. learning rate = 0.1

new_weights, new_bias = logistic_regression_trick(weights, bias, features, label, learning_rate=0.1, epoch=100)

#print("New Log Loss for p: ", log_loss(new_weights, new_bias, features, label))

# Exercise 6.3: Find p for prediction 0.8
# given sigmoid(3x1 + 2x2 -5) = 0.8, find p = (x1, x2)

#print(sigmoid(1.3862943611198906))  # should be close to 0.8 (refer to a sigmoid table or use calculator)

# np.dot(weights, features) + bias = 1.3862943611198906
# np.dot(weights, features) = 1.3862943611198906 - bias
# weights * features = 1.3862943611198906 + bias
# given that features is an array of two numbers let's split
# w1 * f1 + w2 * f2 = 1.3862943611198906 + bias
# 3 * f1 + 2 * f2 = 1.386294361
# let's assume f2 = 1
# 3 * f1 + 2 * 1 = 1.3862943611198906 + 5
# 3 * f1 = 1.3862943611198906 + 5 - 2
# f1 = (1.3862943611198906 + 5 - 2) / 3
# f2 = 1

features = [ (1.3862943611198906 + 5 - 2) / 3 , 1 ]
print("Features for prediction 0.8:", features)
print("Verification:", prediction([3, 2], -5, features))  # should be close to 0.8
