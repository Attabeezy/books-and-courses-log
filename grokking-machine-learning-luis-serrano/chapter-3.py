# LINEAR REGRESSION
import random
import numpy as np

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
import matplotlib.pyplot as plt

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
