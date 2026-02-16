# LINEAR REGRESSION
import random
import numpy as np
import matplotlib.pyplot as plt

# Coding Linear Regression
# Using the Square Trick
def square_trick(base_price, price_per_room, num_rooms, price, learning_rate):
    """Generates the new parameters for
    linear regression using the square trick.   

    Args:
        base_price (float): The base price of the property.
        price_per_room (float): The price per room of the property.
        num_rooms (int): The number of rooms in the property.
        price (float): The actual price of the property.
        learning_rate (float): The learning rate for the gradient descent.

    Returns:
        float: The updated base price.
        float: The updated price per room.
    """
    predicted_price = base_price + price_per_room * num_rooms
    base_price += learning_rate * (price - predicted_price)
    price_per_room += learning_rate * num_rooms * (price - predicted_price)
    return base_price, price_per_room

# Using the absolute trick
def absolute_trick(base_price, price_per_room, num_rooms, price, learning_rate):
    """Generates the new parameters for
    linear regression using the absolute trick.

    Args:
        base_price (float): The base price of the property.
        price_per_room (float): The price per room of the property.
        num_rooms (int): The number of rooms in the property.
        price (float): The actual price of the property.
        learning_rate (float): The learning rate for the gradient descent.

    Returns:
        float: The updated base price.
        float: The updated price per room.
    """
    
    predicted_price = base_price + price_per_room + num_rooms
    if price > predicted_price:
        price_per_room += learning_rate * num_rooms
        base_price += learning_rate
    else:
        price_per_room -= learning_rate * num_rooms
        base_price -= learning_rate
    return base_price, price_per_room

# Linear Regression Algorithm
def linear_regression(features, labels, learning_rate = 0.01, epochs = 1000):
    """Performs linear regression on the given features and labels.

    Args:
        features (list of tuples): The features of the data points.
        labels (list of floats): The labels of the data points.
        learning_rate (float, optional): The learning rate for the gradient descent. Defaults to 0.01.
        epochs (int, optional): The number of iterations for training. Defaults to 1000.

    Returns:
        tuple: The final parameters (base_price, price_per_room) after training.
    """
    # Initialize parameters
    base_price = random.random()
    price_per_room = random.random()

    for epoch in range(epochs):
        i = random.randint(0, len(features) - 1)
        num_rooms = features[i]
        price = labels[i]
        price_per_room, base_price = square_trick(
            base_price, price_per_room, num_rooms, price, learning_rate=learning_rate
        )
        
    return base_price, price_per_room

# loading and plotting data
features = np.array([1, 2, 3, 5, 6, 7])
labels = np.array([155, 197, 244, 356, 407, 448])

# Plotting data
plt.scatter(features, labels, color='blue')
plt.xlabel('Number of Rooms')
plt.ylabel('Price')
plt.title('House Prices')
plt.show()

# Running Linear Regression
base_price, price_per_room = linear_regression(features, labels, learning_rate=0.01, epochs=10000)
# Expected output: (base_price, price_per_room) close to (100, 50)

# Using the learned parameters to make predictions
num_rooms = 4
predicted_price = base_price + price_per_room * num_rooms

# root mean squared error function
def rmse(labels, predictions):
    n = len(labels)
    differences = np.subtract(labels, predictions)
    return np.sqrt(np.sum(differences **2) / n)

"""
Summary:
• Regression is an important part of machine learning. It consists of training an algorithm
with labeled data and using it to make predictions on future (unlabeled) data.
• Labeled data is data that comes with labels, which in the regression case, are numbers.
For example, the numbers could be prices of houses.
• In a dataset, the features are the properties that we use to predict the label. For example,
if we want to predict housing prices, the features are anything that describes the house
and which could determine the price, such as size, number of rooms, school quality,
crime rate, age of the house, and distance to the highway.
• The linear regression method for predicting consists in assigning a weight to each of the
features and adding the corresponding weights multiplied by the features, plus a bias.
• Graphically, we can see the linear regression algorithm as trying to pass a line as close as
possible to a set of points.
• The way the linear regression algorithm works is by starting with a random line and then
slowly moving it closer to each of the points that is misclassified, to attempt to classify
them correctly.
• Polynomial regression is a generalization of linear regression, in which we use curves
instead of lines to model our data. This is particularly useful when our dataset is nonlinear.
• Regression has numerous applications, including recommendation systems, ecommerce,
and health care.
"""

# Exercise 3.1
y = 0 # 45 years adult
a = 1 # 45 years adult
m = 1 # uses mobile for website
d = 0 # doesn't use desktop

i = 0.8 * d + 0.5 * m + 0.5 * y + 0.2 * a + 1.5
print(i)


# Exercise 3.2

# a
# 1. number of hours of exercise per week (positive number)
# 2. number of cigarettes smoked per week (negative number)
# 3. number of family members with heart disease (negative number)
# 4. number of siblings of patient (zero impact)
# 5. whether patient has been hospitalized (positive number)

# b
# bias is a positive number


# Exercise 3.3

def predicted_price(size):
    return (2 * size) + 50

sizes = [100, 200, 200, 250, 325]

predicted_prices = [predicted_price(size) for size in sizes]

mean_absolute_error = np.mean(np.abs(np.array([150, 250, 300, 400, 500]) - np.array(predicted_prices)))
print(mean_absolute_error)

root_mean_squared_error = rmse(np.array([150, 250, 300, 400, 500]), np.array(predicted_prices))
print(root_mean_squared_error)


# Exercise 3.4
# Our goal: move line y = 2x + 3 closer to (x,y) = (5,15) using the tricks
# use learning rate = 0.01

predicted_y = 2 * 5 + 3  # initial prediction
learning_rate = 0.01
base, slope = 3, 2

# using square trick
base, slope = square_trick(base, slope, 5, 15, learning_rate)
print(f"Square Trick -> New base: {base}, New slope: {slope}")

# using absolute trick
base, slope = absolute_trick(base, slope, 5, 15, learning_rate)
print(f"Absolute Trick -> New base: {base}, New slope: {slope}")