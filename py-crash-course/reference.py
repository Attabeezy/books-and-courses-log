class Car():
    """a simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """initializing attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """printing a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)
    
    def upgrade_battery(self):
        if self.battery_size !=85:
            self.battery_size = 85

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class Restaurant():
    """this is a model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        "initializing the name and cuisine type of restaurant"
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """describes the restaurant by name and type"""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The restaurant serves " + self.cuisine_type.title() + " food.")
    
    def open_restaurant(self):
        """Simulate the restaurant being opening"""
        print("\nThe " + self.restaurant_name.title() + " is open!")
    
    def set_number_served(self, number_served):
        """sets the number of customers served"""
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        """increment of the number of customers served"""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']
    
    def get_flavors(self):
        print("These are the flavors we have:")
        for flavor in self.flavors:
            print("\t" + flavor)


class User():
    def __init__(self, first_name, last_name, gender, bio):
        """initializing object with initial attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.bio = bio
        self.login_attempts = 0
        self.full_name = self.first_name + " " + self.last_name
    
    def describe_user(self):
        """a summary of user's info"""
        print("\nThe user is " + self.full_name.title() + ".")
        print("The user is a " + self.gender + ".")
        print("The user's bio: \n\t" + self.bio)
    
    def greet_user(self):
        """a personalized greeting to the user"""
        print("\nHello!, " + self.full_name.title() + ". Welcome to our platform.")
    
    def increment_login_attempts(self):
        """increases the number of login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """resets the login attempts to 0"""
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, gender, bio):
        super().__init__(first_name, last_name, gender, bio)
        self.privileges = ['can add post', 'can delete', 'can ban user']
    
    def show_privileges(self):
        print("\nThe Admin has the following privileges: ")
        for privilege in self.privileges:
            print("\t" + privilege)

class User():
    def __init__(self, first_name, last_name, gender, bio):
        """initializing object with initial attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.bio = bio
        self.login_attempts = 0
        self.full_name = self.first_name + " " + self.last_name
    
    def describe_user(self):
        """a summary of user's info"""
        print("\nThe user is " + self.full_name.title() + ".")
        print("The user is a " + self.gender + ".")
        print("The user's bio: \n\t" + self.bio)
    
    def greet_user(self):
        """a personalized greeting to the user"""
        print("\nHello!, " + self.full_name.title() + ". Welcome to our platform.")
    
    def increment_login_attempts(self):
        """increases the number of login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """resets the login attempts to 0"""
        self.login_attempts = 0

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete', 'can ban user']