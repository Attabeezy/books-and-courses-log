### If Statements ###
# conditional tests which are used to check if a condition is true or false
# if statement
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
        
# Checking for equality and inequality
car = "bmw"
print(car == "bmw") # True
print(car == "audi") # False


# Checking for equality and inequality
# testing for equality is case sensitive
car = "Audi"
print(car == "audi") # False
print(car.lower() == "audi") # True

# Checking for inequality
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Numerical comparisons
age = 18
print(age == 18) # True
print(age != 18) # False

answer = 17

if answer != 42:
    print("\nThat is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# Checking multiple conditions
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)

print((age_0 >= 21) and (age_1 >= 21))

print((age_0 >= 21) or (age_1 >= 21))

# checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)

# checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
# Boolean Expressions
game_active = True
can_edit = False

## Try it Yourself
# 5-1 Conditional Tests
food = "Gob3"
print("Is food == 'Gob3'? I predict True.")
print(food == "Gob3")

print("\nIs food == 'fried rice'? I predict False.")
print(food == 'fried rice')

# 5-2 More Conditional Tests
access = "Granted"
print(access == 'Granted')
print(access != "Not Granted")
print(access == access.lower())

number = 4
print(number > 3, "This will be True")
print(number > 5, "This will be False")
print(number < 5, "This will be True")
print(number < 3, "This will be False")
print(number <= 5, "This is True")
print(number >= 4, "This is True")
print(number >= 5, "This is False")
print(number <= 4, "This is True \n")

print(number == 4 and number < 5, "True")
print(number == 3 and number < 2, "False")
print(number == 4 and number < 2, "False")
print(number == 3 and number < 5, "False")
print(number == 4 or number < 2, "True")
print(number == 3 or number < 5, "True")

items = [1, 2, 3, 4, 5]
for item in items:
    if item == 5:
        print("5 is in items")
    else:
        print("5 is not in the list")

for item in items:
    if item != 6:
        print("6 is not in list")
    else:
        print("items is wrong")

# If Statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# If-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# If-elif-else Chain
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("Your admission cost is $10")


# Case 2
# If-elif-else Chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
    
print("Your admission cost is $"+str(price) + ".")

# Senior discount
age = 7
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $"+str(price) + ".")

## Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding extra cheese.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")

## Testing for when Multiple Choice would not work with elif
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
    print("Adding extra cheese.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
    
print("\nFinished making your pizza!")

## Try it yourself
# 5-3 Alien Colors #1
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points")

alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points")

# 5-4 Alien Colors #2
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points for shooting the alien")
else:
    print("You just earned 10 points")

# 5-5 Alien Colors #3
alien_color = "green"
if alien_color == "green":
    print("You just earned 5")
if alien_color == "yellow":
    print("You just earned 10 points")
if alien_color == "red":
    print("You just earned 15 points")

# 5-6 Stages of Life
age = 21

if age < 2:
    print("you are a baby")
if age >= 2 and age < 4:
    print("you are a toddler")
if age >= 4 and age < 13:
    print("you are a kid")
if age >= 13 and age < 20:
    print("you are a teenager")
if age >= 20 and age < 65:
    print("you are an adult")
else:
    print("you are an elder")

# 5-7 Favorite Fruit
favorite_fruit = ["banana", "groundnut", "apple"]

if "banana" in favorite_fruit:
    print("You really like bananas!")
if "groundnut" in favorite_fruit:
    print("You really like groundnuts!")
if "apple" in favorite_fruit:
    print("You really like apples!")

# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we're out of green peppers right now.")
    else:
        print("Adding "+ requested_topping + ".")

print("\nFinished making your pizza!")



requested_toppings =[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizzas?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping +".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
    
print("\nFinished making pizza!")

## Try It Yourself
# 5-8 Hello Admin
users = ['john', 'ben', 'admin', 'joe', 'sam']

for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+ user + ", thank you for logging in again.")

# 5-9 No Users
users = []

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+ user + ", thank you for logging in again.")
else:
    print("we need some users!")

# 5-10 Checking Usernames:
current_users = ['john', 'ben', 'admin', 'joe', 'sam']
new_users = ['mike', 'steve', 'ned', 'joe', 'sam']

for user_name in new_users:
    if user_name.lower() in current_users:
        print("please enter a new user name")
    else:
        print("user name is available")

# 5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number >= 4 or number <= 9:
        print(str(number) + "th")
