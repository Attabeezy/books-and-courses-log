import random
import numpy as np

"""
Summary
• Classification is an important part of machine learning. It is similar to regression in that
it consists of training an algorithm with labeled data and using it to make predictions on
future (unlabeled) data. The difference from regression is that in classification, the
predictions are categories, such as yes/no, spam/ham, and so on.
• Perceptron classifiers work by assigning a weight to each of the features and a bias. The
score of a data point is calculated as the sum of products of the weights and features, plus
the bias. If the score is greater than or equal to zero, the classifier predicts a yes.
Otherwise, it predicts a no.
• For sentiment analysis, a perceptron consists of a score for each of the words in the
dictionary, together with a bias. Happy words normally end up with a positive score, and
sad words with a negative score. Neutral words such as the likely end up with a score close
to zero.
• The bias helps us decide if the empty sentence is happy or sad. If the bias is positive, then
the empty sentence is happy, and if it is negative, then the empty sentence is sad.
• Graphically, we can see a perceptron as a line trying to separate two classes of points,
which can be seen as points of two different colors. In higher dimensions, a perceptron is
a hyperplane separating points.
• The perceptron algorithm works by starting with a random line and then slowly moving
it to separate the points well. In every iteration, it picks a random point. If the point is
correctly classified, the line doesn’t move. If it is misclassified, then the line moves a little
bit closer to the point to pass over it and classify it correctly.
• The perceptron algorithm has numerous applications, including spam email detection,
recommendation systems, e-commerce, and health care.
"""

features = np.array([[1,0],[0,2],[1,1],[1,2],[1,3],[2,2],[2,3],[3,2]])
labels = np.array([0,0,0,0,1,1,1,1])

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

print(perceptron_algorithm(features, labels))