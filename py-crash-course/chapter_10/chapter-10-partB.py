# Using json.dump() and json.load()
# number_writer.py
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


# number_reader.py
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# saving and reading User-Generated Data
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

# using stored name to print greeting message
# greet_user.py
filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# remember me
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

# refactoring
def greet_user():
    """Greet the user by name."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()

# refactoring
# getting stored user
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()


# try it yourself
# 10-11 Favorite Number

number = input("Number: ")

file_name = "number.json"

with open(file_name, 'w') as file_object:
    json.dump(number, file_object)

with open(file_name, 'r') as file_object:
    number = json.load(file_object)
    print(number)

# 10-12 Favorite Number Remembered
file_name = "number.json"
try:
    with open(file_name, 'r') as file_object:
        number = json.load(file_object)
    print("We remembered! Your favorite number is " + str(number))
except (FileNotFoundError, json.JSONDecodeError):
    number = input("Number: ")
    with open(file_name, 'w') as file_object:
        json.dump(number, file_object)
    print("We'll remember your number " + str(number))

# 10-13 Verify User
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    current_user = input("what is your user name: ")
    if current_user == get_stored_username():
        username = get_stored_username()
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()