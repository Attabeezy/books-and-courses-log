"""
Summary
• When it comes to training models, many problems arise. Two problems that come up
quite often are underfitting and overfitting.
• Underfitting occurs when we use a very simple model to fit our dataset. Overfitting
occurs when we use an overly complex model to fit our dataset.
• An effective way to tell overfitting and underfitting apart is by using a testing dataset.
• To test a model, we split the data into two sets: a training set and a testing set. The
training set is used to train the model, and the testing set is used to evaluate the model.
• The golden rule of machine learning is to never use our testing data for training or
making decisions in our models.
• The validation set is another portion of our dataset that we use to make decisions about
the hyperparameters in our model.
• A model that underfits will perform poorly in the training set and in the validation set. A
model that overfits will perform well in the training set but poorly in the validation set.
A good model will perform well on both the training and the validation sets.
• The model complexity graph is used to determine the correct complexity of a model, so
that it doesn’t underfit or overfit.
• Regularization is a very important technique to reduce overfitting in machine learning
models. It consists of adding a measure of complexity (regularization term) to the error
function during the training process.
• The L1 and L2 norms are the two most common measures of complexity used in
regularization.
• Using the L1 norm leads to L1 regularization, or lasso regression. Using the L2 norm
leads to L2 regularization, or ridge regression.
"""