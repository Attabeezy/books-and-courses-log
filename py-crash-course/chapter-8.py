### Functions ###
# defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
greet_user('sarah')

# try it yourself
# 8-1 message
def display_message():
    print("I'm learning about functions in this chapter")

display_message()

# 8-2 favorite book
def favorite_book(title):
    print("One of my favorite books is " + title.title())

favorite_book("the man who solved the market")

## Passing Arguments
# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
# multiple function calls
describe_pet('dog', 'willie')
# order matters
describe_pet('harry', 'hamster')

# keyword arguments, the order doesn't matter
describe_pet(animal_type='hamster', pet_name='harry')

describe_pet(pet_name='harry', animal_type='hamster')

# default value
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet('willie')

describe_pet(pet_name='harry', animal_type='hamster')

# equivalent function calls
# a dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# avoiding argument errors
# unmatched arguments: fewer or more arguments than needed
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# uncomment the next line
#describe_pet() #at least first name or error

## try it yourself
# 8-3 T-shirts
def make_shirt(size, text):
    print("\nthis shirt is size " + size + " and has the inscription '" + text + "' written on it")

make_shirt('small', 'YAML')
make_shirt(size='small', text='YAML')

# 8-4 Large Shirts
def make_shirt(size = 'large', text='I love Python'):
    print("\nthis shirt is size " + size + " and has the inscription '" + text + "' written on it")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', text='I love coding')

# 8-5 Cities
def describe_city(city, country = 'Ghana'):
    print("\n" + city.title() + " is in " + country.title())

describe_city('Accra')
describe_city('Takoradi')
describe_city('Rio', 'Brazil')

# Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jim', 'hendrix')
print(musician)

# Making an Argument Optional
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# making middle_name optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = '\n' + first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = '\n' + first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jim', 'hendrix')
print(musician)

musician= get_formatted_name('jim', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    print("\n")
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jim', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jim', 'hendrix', age = 27)
print(musician)


## Using a Function with a While loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop!
while True:
    break # remove this break to make code work!!!
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

## try it yourself
# 8-6 City Names
def city_country(city, country):
    print("\n" + city.title() + ", " + country.title())

city_country("Accra", "Ghana")

# 8-7 Album
def make_album(artist, album, tracks = ""):
    print("\nLet's make an album!")
    if tracks:
        print({"Artist Name" : artist,
               "Album Name": album,
               "tracks" : tracks})
    else:
        print({"Artist Name" : artist,
               "Album Name": album,})
#  Continuation for 8-8 User Album
while True:
    break # remove break to run code
    print("Enter Album Details \n (press 'q' to quit)")
    
    artist = input("artist name: ")
    if artist == 'q':
        break
    
    album = input("album name: ")
    if album == 'q':
        break
    
    tracks = input("number of tracks: ")
    if tracks == 'q':
        break
    make_album(artist, album, tracks)

# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Simulate printing each design, until none re left.
# Move each design to completed_models after printing.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

# Display all completed models.
def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

# Modifying a List in a Function
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("\n")

# try it yourself
# 8-9 magicians
magicians = ['Merlin', 'Houdini', 'Copperfield', 'Blaine']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

show_magicians(magicians)

# 8-10 Great Magicians
def make_great(magicians):
    """Add 'the Great' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"

make_great(magicians)
show_magicians(magicians)

# 8-11 Unchanged Magicians
magicians = ['Merlin', 'Houdini', 'Copperfield', 'Blaine']

def make_great(magicians):
    """Add 'the Great' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"
        return magicians

new_magicians = make_great(magicians[:])
print(new_magicians)
print(magicians)


## Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

## Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

## Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything
    we know about users."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field='physics')

print(user_profile)

# try it yourself
# 8-12 sandwiches

def sandwich_maker(name, *addons):
    """making sandwich with my addons"""
    print(" Hello " + name + ", the your sandwich with: ")
    for addon in addons:
        print("\t- " + addon)
    
    print("is ready")

sandwich_maker("Benjamin", "Meat", "Pepper", "Gravy")

# 8-3 User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything
    we know about users."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('benjamin', 'attabra', what_are_you_doing = 'learning python', why='thats how we get paid', why_again = 'mama needs a bugatti')

print(user_profile)

# 8-14 Cars
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    
    for key, value in car_info.items():
        car[key] = value
    
    return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)