## Dictionaries
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Working with dictionaries
# A dictionary is a collection of key-value pairs.

alien_0 = {'color': 'green', 'points': 5}

# simple dictionary
alien_0 = {'color': 'green'}
# getting the value associated with a key
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# adding a new key-value pair
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

## Alien speed for changing position
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

## Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

## Try It Yourself
# 6-1. Person: Use a dictionary to store information about a person you know.
Person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

# 6-2. Favorite Numbers: Use a dictionary to store people's favorite numbers.
favorite_numbers = {
    'Ama': 1,
    'Kwame': 2,
    'Akosua': 3,
    'Kofi': 4,
    'Abena': 5,
}
# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
Glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'An unordered collection of unique items.',
    'string': 'A sequence of characters.',
}

# Looping Through a Dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# Looping Through Favorite Languages
for name, language in favorite_languages.items():
    print(name.title() +
          "'s favorite language is " +
          language.title() +
          ".")

# Checking for a Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())
    
# Checking for a Keys in a Dictionary is default
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() +
              "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# Looping Through a Dictionary in Order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
# Looping Through All Values in a Dictionary
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Set to get unique values
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Try it yourself
# 6-4 Glossary 2: A Python dictionary can be used to model an actual dictionary.
glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'An unordered collection of unique items.',
    'string': 'A sequence of characters.',
}

# 6-5 Rivers: Use a dictionary to store information about a river.
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'usa',
}

for river, country in rivers.items():
    print(" The " +
          river.title() +
          " runs through " +
          country.title() +
          ".")

# name of each river
for river in rivers.keys():
    print(river.title())

# name of each country
for country in rivers.values():
    print(country.title())

# 6-6 Polling: Use the code in 6-4, but instead of printing the results right away,
# store the results in a dictionary. At the end of the poll, print the results.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

respondents = ['jen', 'edward', 'sam', 'chris']

for respondent in respondents:
    if respondent in favorite_languages.keys():
        print('Thank you for responding, ' +
              respondent.title() + '!')
    else:
        print('Please take our poll, ' +
              respondent.title() + '!')

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

# show the first 5
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# changing the color of the first 3 aliens
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# show the first 5
for alien in aliens[:5]:
    print(alien)
print("...")


## List in a dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print("\nYou ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())


## try it yourself
# 6-7 People
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

person2 = {
    'first_name': 'Sam',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Seattle',
}

person3 = {
    'first_name': 'Will',
    'last_name': 'Doe',
    'age': 32,
    'city': 'Los Angeles',
}

People = [person1, person2, person3]

for person in People:
    full_name = person['first_name'] + " " + person['last_name']
    print("\nName: " + full_name)
    print("\tAge: " + str(person['age']))
    print("\tCity: " + person['city'])


# 6-8 Pets
bingo = {"kind": "rabbit",
         "owner": "john"}

rainbow = {"kind": "cat",
         "owner": "sam"}

axe = {"kind": "dog",
         "owner": "alex"}

pets = [bingo, rainbow, axe]

for pet in pets:
    print("\nKind: " + pet['kind'])
    print("Owner: " + pet['owner'])

# 6-9 Favorite Places
favorite_places = {
    "John": "Dubai",
    "Ben": "New York",
    "Sam": "London",
}

for name, place in favorite_places.items():
    print(name + "'s favorite place is " + place)

# 6-10 Favourite NUmbers:
favorite_numbers = {
    'Ama': [1],
    'Kwame': [2],
    'Akosua': [3, 9, 27],
    'Kofi': [4, 16, 64],
    'Abena': [5, 25, 125],
}

for name in favorite_numbers.keys():
    numbers = favorite_numbers[name]
    if len(numbers) == 1:
        print("\n" + name + "'s favorite number is:")
        for number in range(len(numbers)):
            print("\t"+ str(number))
    else:
        print("\n" + name + "'s favorite numbers are:")
        for number in range(len(numbers)):
            print("\t"+str(number))

# 6-11 Cities
cities = {
    "New York":{
        "country": "USA",
        "population": 9000000,
        "fact":"world financial capital",
    },
    "London":{
        "country": "UK",
        "population": 7500000,
        "fact":"home to a lot of history",
    },
   "Vancouver":{
        "country": "Canada",
        "population": 4500000,
        "fact":"Capital of Most Peaceful Country",
    }
}

for city in cities.keys():
    print("Here are the things I like about " + city + ":")
    city_info = cities[city]
    for key, value in city_info.items():
        print("\t" + key + ": " + str(value))
