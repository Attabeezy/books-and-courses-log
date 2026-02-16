## Chapter 3: Introducing Lists
# Example of a list
bicycles = ['trek', 'cannon', 'redline', 'specialized']
print(bicycles)

#Accessing elements in a list
print(bicycles[0]) #first element
print(bicycles[0].title()) #first element in title case

#Index Positions Starting at 0, not 1
print(bicycles[1]) # second element
print(bicycles[3]) # fourth element

#Special Syntax for last element in a list
print(bicycles[-1]) # last element
print(bicycles[-2]) # second to last element

# Using individual values from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 3-1 Names
friends = ['Winston', 'Rodgers', 'Jefferson']
print(friends[0],
      friends[1],
      friends[2])

# 3-2 Greetings
print("Hello " + friends[0] + ", how are you doing today?")
print("Hello " + friends[1] + ", how are you doing today?")
print("Hello " + friends[2] + ", how are you doing today?")


# 3-3 Your Own List
# Create a list of your favorite foods and print it out
foods = ['rice', 'beans', 'yam', 'plantain']
print("Can I have "+foods[0] + " for today?")
print("Can I have "+foods[1] + " for today?")
print("Can I have "+foods[2] + " for today?")
print("Can I have "+foods[3] + " for today?")


#Changing, adding and removing elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #changing the first element
print(motorcycles)

motorcycles.append('honda') #adding an element to the end of the list
print(motorcycles)


# append() method is dynamic, it can be used to add any element to the list
motorcycles = [] #empty list
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting elements into a list
motorcycles.insert(0, 'ducati') #inserting an element at the beginning of the list
print(motorcycles)

del motorcycles[0]
print(motorcycles) #deleting the first element in the list

del motorcycles[1]
print(motorcycles) #deleting the second element in the list which is now the first element

# Removing elements using pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() #removing the last element in the list
print(motorcycles) #printing the list after removing the last element
print(popped_motorcycle) #printing the element that was removed from the list

# example of using pop() method to remove an element from a specific position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop() #removing the last element in the list
print("The Last motorcycle I owned was a " + last_owned.title() +".")

# Poppping items from any position in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) #removing the first element in the list
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')   #removing an element by value
print(motorcycles) #printing the list after removing the element

# You can also use remove() to work with the value that was removed
# Example: removing a value and using it in a message
motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
too_expensive = 'ducati'  #storing the value to be removed in a variable
motorcycles.remove(too_expensive) #removing an element by value
print(motorcycles) #printing the list after removing the element
print("\nA " + too_expensive.title() + " is too expensive for me.") #using the value that was removed in a message

# Exercises
# 3-4 Guest List
guests = ['Winston', 'Rodgers', 'Jefferson']
print(guests[0] + " is invited to the party.")
print(guests[1] + " is invited to the party.")
print(guests[2] + " is invited to the party.")

# 3-5 Changing Guest List
cant_come = guests.pop(1) #removing an element from the list
print(cant_come + " can't make it to the party.")
guests.append('Sena')
print(guests[2] + " is invited to the party.")

# 3-6 More Guests
print("I found a bigger table, so I can invite more guests.")
guests.insert(0, 'Gabriel') #inserting an element at the beginning of the list
guests.insert(2, 'Samuel') #inserting an element at the third position in the list
guests.append('Esther') #adding an element to the end of the list

print(guests[0] + " is invited to the party.")
print(guests[1] + " is invited to the party.")
print(guests[2] + " is invited to the party.")
print(guests[3] + " is invited to the party.")
print(guests[4] + " is invited to the party.")
print(guests[5] + " is invited to the party.")

# 3-7 Shrinking Guest List
sorry_message = "! Sorry, I can only invite two people to dinner."
first_shrink = guests.pop(0) #removing an element from the list
print(first_shrink + sorry_message) #printing the message with the name of the person who was removed from the list
second_shrink = guests.pop(1) #removing the now second element from the list
print(second_shrink + sorry_message) #printing the message with the name of the person who was removed from the list
third_shrink = guests.pop(2) #removing the now third element from the list
print(third_shrink + sorry_message) #printing the message with the name of the person who was removed from the list
fourth_shrink = guests.pop() #removing the last element from the list
print(fourth_shrink + sorry_message) #printing the message with the name of the person who was removed from the list

del guests[0] #deleting the first element in the list
del guests[0] #deleting the first element in the list

print(guests) #printing the list after removing the elements
print("I am sorry that I can't invite you to dinner.") #printing a message to the people who were removed from the list


# Organizing a list
# Sorting a list permanently with sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sorting the list in alphabetical order
print(cars)

cars.sort(reverse=True) #sorting the list in reverse alphabetical order
print(cars)

# Sorting a list temporarily with sorted() function not method
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#note: Sorting a list alphabetically is a bit more complicated when all the values are not in
#lowercase. There are several ways to interpret capital letters when you’re deciding on
#a sort order, and specifying the exact order can be more complex than we want to deal
#with at this time. However, most approaches to sorting will build directly on what you
#learned in this section.

# Reversing the order of a list with reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Finding the length of a list with len() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
number_of_cars = len(cars)
print(number_of_cars)


## Try it yourself
# 3-8 Seeing the World
# Create a list of places you want to visit and print it out in its original order.
places = ['Singapore', 'London', 'New York', 'San Francisco']

# print in original order
print(places)

# Print your list in alphabetical order without modifying the actual list.
print(sorted(places))
# Show it in its original order again.
print(places)

# Print your list in reverse alphabetical order without modifying the actual list.
print(sorted(places, reverse=True))
# Show it in its original order again.
print(places)

# Reverse the order of your list. Print it to show that its order has changed.
places.reverse()
print(places)

# Reverse the order again. Print it to show it’s back to its original order.
places.reverse()
print(places)

# Sort your list so it’s stored in its original order. Print the list to show it’s back to its original order.
places.sort()
print(places)

# Sort your list in reverse alphabetical order. Print it to show that its order has changed.
places.sort(reverse=True)
print(places)

# 3-9 Dinner Guests
# Using len() to determine the number of guests
guests = ['Winston', 'Rodgers', 'Jefferson']
number_of_guests = len(guests)
print("There are " + str(number_of_guests) + " guests invited to the party.")

# 3-10 Every Function
# Use every function you’ve learned about in this chapter to print a list of your friends.
programming_languages = ['python', 'java', 'c++', 'javascript']

# Print the original list
print(programming_languages)

# Accessing elements in the list
print(programming_languages[0])  # First element
print(programming_languages[-1])  # Last element

# Modifying an element
programming_languages[1] = 'ruby'
print(programming_languages)

# Adding elements
programming_languages.append('go')
print(programming_languages)

# Inserting elements
programming_languages.insert(2, 'swift')
print(programming_languages)

# Removing elements by index
del programming_languages[3]
print(programming_languages)

# Removing elements using pop()
popped_language = programming_languages.pop()
print(popped_language)
print(programming_languages)

# Removing elements by value
programming_languages.remove('swift')
print(programming_languages)

# Sorting the list permanently
programming_languages.sort()
print(programming_languages)

# Sorting the list in reverse order permanently
programming_languages.sort(reverse=True)
print(programming_languages)

# Sorting the list temporarily
print(sorted(programming_languages))
print(programming_languages)

# Reversing the list
programming_languages.reverse()
print(programming_languages)

# Finding the length of the list
print(len(programming_languages))

# Try it yourself
# 3-11 Intentional Error
# Create a list of your favorite programming languages and print it out.
programming_languages = ['python', 'java', 'c++', 'javascript']
print(programming_languages)
#print(programming_languages[10])  # This will raise an IndexError
# Correcting the error
print(programming_languages[-1])  # Accessing the last valid element