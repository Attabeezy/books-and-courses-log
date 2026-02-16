### User Input and While Loops
# message = input("Tell me something, I will repeat it back to you: ")
message = "Hello!"
print(message)

# writing clear prompts
# name = input("please enter your name: ")
name = "Ben"
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

#name = input(prompt)
name = "Ben"
print("\nHello, " + name + "!")

## Using int() to Accept Numerical Input
#age = input("How old are you? ")
age = "21"
age = int(age)
print(age >= 18)

#height = input("How tall are you, in inches? ")
height = "45"
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older")


# Modulo Operator
print("\n")
print(4 % 3,
      5 % 3,
      6 % 3,
      7 % 3)

# Even or Odd
#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
number = 4
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

## try it yourself
# 7-1 Rental Car
#rental_car = input("what rental car do you want: ")
rental_car = "Toyota"
print("Let me see if I can find you a " + rental_car)

# 7-2 Restaurant Seating
#seat = int(input("how many people are in the dinner group: "))
seat = 7
if seat > 8:
    print("please wait for a table")
else:
    print("Your table is ready!")

# 7-3 Multiples of Ten
#number = int(input("Pick a number: "))
number = 20
if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10")

## Introducing While Loops
# While condition is true, code runs
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

## Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    #message = input(prompt)
    message = 'quit'
    if message != 'quit':
        print(message)

# Using a Flag
# Let's use active as our flag
# flag allows multiple usage of condition and break
active = True
while active:
    #message = input(prompt)
    message = 'quit'
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop
prompt = ("\nPlease enter the name of a city you have visited: ")
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    #city = input(prompt)
    city = 'quit'
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

## Try it yourself
# 7-4 Pizza Toppings
active = True
while active:
    #pizza_topping = input("Enter a pizza topping: ")
    pizza_topping = "quit"
    if pizza_topping == "quit":
        break
    else:
        print("I'll add " + pizza_topping + " to your pizza")

# 7-5 Movie Tickets
active = True
while active:
    #age = input("age: ")
    age = 'quit'
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("your ticket is free!")
    elif age >= 3 and age <=12:
        print("your ticket is $10")
    else:
        print("your ticket is $15")

# 7-6 Three Exits
# Refer to 7-4 and 7-5

# 7-7 Infinity
# Press Ctrl-C to Exit!
active = True
x = 0
x += 1
while active:
    break #remove break to make active
    print(x)

## While Loops with Lists and Dictionaries
# Moving Items from One List to Another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users =[]

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print("\t" + confirmed_user.title())

# removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# filling a dictionary with User Input
responses = {}

# set a flag to indicate that polling is active.
polling_active = False # Set polling_active to True for code to work

while polling_active:
    # Prompt for the person's nme and response.
    name = input("\nWhat is your name: ")
    response = input("Which mountain would you like to climb someday? ")
    
    # store the response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

## try it yourself
# 7-8 Deli
sandwich_orders = ['BLT', 'Club', 'Reuben', 'Pastrami', 'French Dip', 'Italian Sub', 'Cuban', 'Philly Cheese steak', 'Meatball Sub', 'Gyro']

finished_sandwich = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich + " sandwich.")
        finished_sandwich.append(sandwich)
        print("Your " + sandwich + " has been made.")

# 7-9 No Pastrami

sandwich_orders = ['BLT', 'Club', 'Pastrami', 'Reuben', 'Pastrami', 'French Dip', 'Italian Sub', 'Pastrami', 'Cuban', 'Philly Cheese steak', 'Meatball Sub', 'Gyro']

finished_sandwich = []

print('\n --- New List ---')

print("deli has run out of Pastrami")
while 'Pastrami' in sandwich_orders:
    break # remove break to run code
    sandwich_orders.remove('Pastrami')

print('\n --- New List ---')

while sandwich_orders:
    break # remove break to run code
    for sandwich in sandwich_orders:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich + " sandwich.")
        finished_sandwich.append(sandwich)
        print("Your " + sandwich + " has been made.")

# 7-10 Dream Vacation
polling_active = True
vacation_poll = {}

while polling_active:
    name = input("your name: ")
    poll = input("If you could visit one place in the world, where would you go: ")
    vacation_poll[name] = poll
    
    looper = input("Anymore? \n\tPress Enter to add more: \n\tType 'quit' to exit \n")
    
    if looper != "quit":
        continue
    elif looper == "quit":
        polling_active = False
    
print(" --- Responses --- ")

for name, poll in vacation_poll.items():
    print(name + "'s Vacation Destination is " + poll)