from collections import OrderedDict
from random import randint

import reference
from reference import Car
from reference import ElectricCar
from reference import *
from reference import Restaurant
from reference import Admin

# Importing a Single Class
# from car  import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Storing Multiple Classes in a Module
# from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing Multiple Classes from a Module
# from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# Importing an Entire Module
# import car (refer to the top)
my_beetle = reference.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = reference.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# Importing All Classes from a Module
# not recommended since we don't know actually used classes
# from car import * (refer to the top)

# Importing a Module into a Module
# Having Car Class in one module and ElectricCar in another,
# We import both so that ElectricCar can rely on Car
# from car import Car
# from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# try it yourself
# 9-10 Imported Restaurant
my_restaurant = Restaurant('Calabash', 'Rice')
my_restaurant.describe_restaurant()

# 9-11 Imported Admin
my_admin = Admin("Benjamin", "Attabra", "Male", "This is the Admin")
my_admin.show_privileges()

# 9-12 Multiple Modules
your_admin = Admin("Hannah", "Fry", "Female", "Works at Cambridge")
your_admin.show_privileges()

print("\n")
# The Python Standard Library
# from collections import OrderedDict (refer to the top)
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# try it yourself
# 9-13 OrderedDict Rewrite
# from collections import OrderedDict (refer to the top)
print("\n")
glossary = OrderedDict()

glossary['list'] = 'A collection of items in a particular order.'
glossary['tuple'] = 'An immutable list.'
glossary['dictionary'] = 'A collection of key-value pairs.'
glossary['set'] = 'An unordered collection of unique items.'
glossary['string'] = 'A sequence of characters.'

for datatype, meaning in glossary.items():
    print(datatype.title() + ": " + meaning)

# 9-14 Dice
# from random import randint (refer to the top)
x = randint(1, 6)

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        print("It fell on side " + str(self.sides))

my_die = Die(6)

for i in range(10):
    my_die.roll_die()

# 9-15 Python Module of the Week
# check out http://pymotw.com/