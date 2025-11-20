"""Summary
• When it comes to training models, many problems arise. Two problems that come up
quite often are under fitting and over fitting.
• Under fitting occurs when we use a very simple model to fit our dataset. Overfitting
occurs when we use an overly complex model to fit our dataset.
• An effective way to tell over fitting and under fitting apart is by using a testing dataset.
• To test a model, we split the data into two sets: a training set and a testing set. The
training set is used to train the model, and the testing set is used to evaluate the model.
• The golden rule of machine learning is to never use our testing data for training or
making decisions in our models.
• The validation set is another portion of our dataset that we use to make decisions about
the hyperparameters in our model.
• A model that under fits will perform poorly in the training set and in the validation set. A
model that over fits will perform well in the training set but poorly in the validation set.
A good model will perform well on both the training and the validation sets.
• The model complexity graph is used to determine the correct complexity of a model, so
that it doesn’t under fit or over fit.
• Regularization is a very important technique to reduce over fitting in machine learning
models. It consists of adding a measure of complexity (regularization term) to the error
function during the training process.
• The L1 and L2 norms are the two most common measures of complexity used in
regularization.
• Using the L1 norm leads to L1 regularization, or lasso regression. Using the L2 norm
leads to L2 regularization, or ridge regression.
"""

# Exercise 4.1
# a. Model 3
# b. Model 4 is under fitting the data because it does poorly on both training (1.9) and testing (2.3)
# c. Model 1 is over fitting the data because it does well on training (0.1) and poorly on testing (1.8)

# Exercise 4.2
"""_summary_
given dataset with X & y; model y_pred = 2x^2 -5x + 4,
determine lasso regression error (using L1 norm) and ridge regression error (using L2 norm) given lambda = 0.1
"""
X = [1, 2, 3, 4, 5]
Y = [2, 2.5, 6, 14.5, 34]
    
def model(x):
    return (2 * (x ** 2)) - (5 * x) + 4

#calculate lasso and ridge regression errors

l1_norm = abs(2) + abs(-5) + abs(4)
l2_norm = (2 ** 2) + ((-5) ** 2) + (4 ** 2)
total_error = 0
lambda_ = 0.1



for i, x in enumerate(X):
    y_pred = model(x)
    error = abs(Y[i] - y_pred)
    total_error += error

lasso_error = total_error + (lambda_ * l1_norm)
ridge_error = total_error + (lambda_ * l2_norm)

#print("Lasso Regression Error:", lasso_error)
#print("Ridge Regression Error:", ridge_error)
