## Working With Lists ##
# printing names of magicians
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
# Suggested naming convention for variables for for loops
# Use singular form of the variable name for the loop variable
# Use plural form of the variable name for the list

# Example:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# Doing more with for loops
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#Doing something after the for loop
print("thank you, everyone. That was a great magic show!")

# Avoiding indentation errors
# Indentation errors are common in Python, especially when using loops and conditionals.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
#print(magician) # This will raise an IndentationError because the print statement is not indented correctly.
# Correct indentation
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#forgetting to indent additional lines of code
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
# This will print the last magician's name outside the loop, which is not intended.

#indenting unnecessary lines of code
message = "Hello Python world!"
#    print(message) # This will raise an IndentationError because the print statement is indented incorrectly.

# Indenting Unnecessary after the loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
#    print("thank you, everyone. That was a great magic show!") # This will raise an IndentationError because the print statement is indented incorrectly.

# forgetting the colon
magicians = ['alice', 'david', 'carolina']
#for magician in magicians
#    print(magician)
    
    
# Try It Yourself 4-1
# Pizzas
pizzas = ['pepperoni', 'margherita', 'bbq chicken']
for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I really enjoy pizza!")

# Try It Yourself 4-2
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(animal)
    
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")

# Making numerical lists
# Using the range() function to generate a list of numbers
for value in range(1, 5):
    print(value)

# numbers between 1 and 5
numbers = list(range(1, 6))
for number in numbers:
    print(number)
    
# Using range() to create a list of even numbers
even_numbers = list(range(2, 11, 2))
for even_number in even_numbers:
    print(even_number)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value**2 for value in range(1, 11)]
print(squares)

# Try It Yourself 4-3
# Counting to Twenty
numbers = [number for number in range(1, 21)]
print(numbers)

# Try It Yourself 4-4
# One Million
#for number in range(1, 1000001):
#    print(number)

# Try It Yourself 4-5
# Summing a Million
print(sum(range(1, 1000001)))
print(min(range(1, 1000001)))
print(max(range(1, 1000001)))

# Try It Yourself 4-6
# Odd Numbers
odd_numbers = [number for number in range(1, 21, 2)]
print(odd_numbers)

# Try It Yourself 4-7
# Threes
threes = [number for number in range(3, 31, 3)]
print(threes)

# Try It Yourself 4-8
# Cubes
cubes = [number**3 for number in range(1, 11)]
print(cubes)

# Try It Yourself 4-9
# Cube Comprehension
cubes = [number**3 for number in range(1, 11)]
print(cubes)

# Working with part of a list
players = ['charles', 'martin', 'michael', 'john', 'james']
print(players[0:3]) # first three players
print(players[1:4]) # middle three players
print(players[2:5]) # last three players
print(players[:4]) # first four players
print(players[2:]) # last three players
print(players[-3:]) # last three players

## Looping through a slice ##
players = ['charles', 'martin', 'michael', 'john', 'james']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

## Copying a list ##
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy new favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#this doesn't work because friend_foods is a reference to my_foods
# This will change the original list
friend_foods = my_foods.copy()

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy new favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Try It Yourself 4-10
# Slices
# first three items in the list
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("The first three items in the list are:")
print(my_foods[:3])

# middle three items in the list
print("The middle three items in the list are:")
print(my_foods[1:4])

# last three items in the list
print("The last three items in the list are:")
print(my_foods[2:5])

# Try it yourself 4-11
# My Pizzas, Your Pizzas
pizzas = ["pepperoni", "margherita", "bbq chicken"]
friend_pizzas = ["pepperoni", "margherita", "bbq chicken", "hawaiian", "vegetarian"]
pizzas.append("meat_lovers")

friend_pizzas.append("seafood")
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# Try It Yourself 4-12
# More Loops
# Using for loops to print each list of foods
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)


## Tuples ##
# A tuple is a collection of items that are ordered and unchangeable.
# Tuples are defined using parentheses () instead of square brackets [].

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 # This will raise a TypeError because tuples are immutable.

for dimension in dimensions:
    print(dimension)
    
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

## Try It Yourself 4-13
# Buffet
buffet = ("pizza", "falafel", "carrot cake", "cannoli", "ice cream")
print("The buffet includes:")
for food in buffet:
    print(food)

# buffet[0] = "sushi" # This will raise a TypeError because tuples are immutable.
buffet = ("sushi", "pasta", "salad", "cannoli", "ice cream")
for food in buffet:
    print(food)

    # Ensure the code follows PEP 8 by adding proper spacing and line breaks
    # No additional functionality is added, only formatting changes

    # Example of PEP 8 formatting
    # Adding a blank line before and after function definitions or class definitions
    # Adding spaces around operators and after commas
    # Limiting lines to 79 characters
    # The code above already follows most PEP 8 guidelines.
