# Classes
# creating the dog class
class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is the now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolling over!")

# making an instance from a class
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My do is " + str(my_dog.age) + " years old.")

# calling methods
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

# creating multiple instances
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's names is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

# try it yourself
# 9-1 restaurant
class Restaurant():
    """this is a model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        "initializing the name and cuisine type of restaurant"
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """describes the restaurant by name and type"""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The restaurant serves " + self.cuisine_type.title() + " food.")
    
    def open_restaurant(self):
        """Simulate the restaurant being opening"""
        print("\nThe " + self.restaurant_name.title() + " is open!")
    
restaurant = Restaurant("Eden", "meat lover's")

print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type.title())

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 three restaurants
restaurant_1 = Restaurant("Apple", "sushi")
restaurant_2 = Restaurant("Kish", "mexican")
restaurant_3 = Restaurant("Xenon", "canadian")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9-3 Users
class User():
    def __init__(self, first_name, last_name, gender, bio):
        """initializing object with initial attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.bio = bio
        self.full_name = self.first_name + " " + self.last_name
    
    def describe_user(self):
        """a summary of user's info"""
        print("\nThe user is " + self.full_name.title() + ".")
        print("The user is a " + self.gender + ".")
        print("The user's bio: \n\t" + self.bio)
    
    def greet_user(self):
        """a personalized greeting to the user"""
        print("\nHello!, " + self.full_name.title() + ". Welcome to our platform.")

first_user = User("Benjamin", "Attabra", "Male", "I love Python!")
second_user = User("Hannah", "Fry", "Female", "Teaches at Cambridge")

first_user.describe_user()
first_user.greet_user()

second_user.describe_user()
second_user.greet_user()


# Working with classes and instances
class Car():
    """a simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """initializing attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """return a neatly formatted description name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Modifying Attribute Values
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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Method 1: Modifying attribute values
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Method 2: Modifying an Attribute's Value Through a Method
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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Method 3: Incrementing an Attribute's Value through a method
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

my_used_car = Car('subaru','outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(235000)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# try it yourself
# 9-4 Number Served
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

restaurant = Restaurant("Eden", "meat lover's")

print(restaurant.number_served)
restaurant.number_served = 15
print(restaurant.number_served)

restaurant.set_number_served(25)
print(restaurant.number_served)

restaurant.increment_number_served(11)
print(restaurant.number_served)

# 9-5 Login Attempts
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

first_user = User("Benjamin", "Attabra", "Male", "I love Python!")
second_user = User("Hannah", "Fry", "Female", "Teaches at Cambridge")

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(first_user.login_attempts)

first_user.reset_login_attempts()
print(first_user.login_attempts)


# Inheritance
# Creation and Testing
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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# Defining Attributes and Methods for the Child Class
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

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# overriding methods from the parent class
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

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# Modeling Real-World Objects
# Don't be surprised to be rewrite code several times to arrive at the most efficient approach

# try it yourself
# 9-6 Ice Cream Stand
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

my_stand = IceCreamStand("Icy Cup", "Ice Cream")
print("\n")
my_stand.describe_restaurant()
my_stand.get_flavors()

# 9-7 Admin
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

first_user = User("Benjamin", "Attabra", "Male", "I love Python!")
second_user = User("Hannah", "Fry", "Female", "Teaches at Cambridge")

my_admin = Admin("Samuel", "Nadutey", "Male", "Son of Eric Matthes")
my_admin.show_privileges()

# 9-8 Privileges
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


class Admin(User):
    def __init__(self, first_name, last_name, gender, bio):
        super().__init__(first_name, last_name, gender, bio)
        self.given_privileges = Privileges()
    
    def show_privileges(self):
        print("\nThe Admin has the following privileges: ")
        for privilege in self.given_privileges.privileges:
            print("\t" + privilege)

first_user = User("Benjamin", "Attabra", "Male", "I love Python!")
second_user = User("Hannah", "Fry", "Female", "Teaches at Cambridge")

my_admin = Admin("Samuel", "Nadutey", "Male", "Son of Eric Matthes")
print(my_admin.given_privileges.privileges)
my_admin.show_privileges()

# 9-9 Battery Upgrade
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

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
