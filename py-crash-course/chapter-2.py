####Variables and Simple Data Types
##Part One
##Variables
message = "Hello Python World!"
print(message)

#Modifying a variable's value
message = "Hello Python Crash Course World!"
print(message)

#Error in Variable
#message = "Hello Python Crash Course reader!"
#print(mesage) # type: ignore #mesage is undefined  # noqa: F821

# Computers are strict but they ignore bad spelling
mesage = "Hello Python Crash Course reader!"
print(mesage)

## Strings
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

#another way to combine strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

#storing a message in a variable and then printing that message
message = "Hello, " + full_name.title() + "!"
print(message)

#adding whitespace to strings with tabs or newlines
print("Python")
print("\tPython")

#adding a tab to a string
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping whitespace
favorite_language = ' python '
print(favorite_language)

favorite_language.rstrip() #removes whitespace from the right side of the string

favorite_language.lstrip() #removes whitespace from the left side of the string
print(favorite_language)

favorite_language.strip() #removes whitespace from both sides of the string
print(favorite_language)

#Avoiding syntax errors with Strings
#Using single quotes to avoid syntax errors
message = "One of Python's strengths is its diverse communtiy."
print(message)

#Ending a string with single quotes
#message = 'One of Python's strenght is its diverse community. ' # type: ignore #SyntaxError: invalid syntax
#print(message)
# The above line will cause a syntax error because the string is not properly closed with a matching single quote. To fix this, you can use double quotes to enclose the string, like this:

### Try it yourself
# 2-3 Personal Message
name = "John Doe"
message = "Hello " + name + " woudl you like to learn Python today?"
print(message)

# 2-4 - 6 Name Cases
name = "John Doe"
print(name.lower())
print(name.upper())
print(name.title())

Name = "Benjamin Attabra"
Quote = "Life dey bi"
print(Name + " once said, '" + Quote + "'.")

# 2-7 Stripping Names
name = " Benjamin Attabra "
print(name.lstrip())
print(name.rstrip())

name = "Benjamin \t\n Attabra "
print(name)


##Part Two: Numbers
#Integer Operations
print(2 + 3, #addition
      3 - 2, #subtraction
      2 * 3, #multiplication
      3 / 2, #division
      3 ** 2, #exponent
      10 ** 6, #exponent
      2 + 3*4, #means 2 + (3*4)
      (2 + 3) * 4) #use brackets!

#Floats
print(0.1 + 0.1, #addition
      0.2 + 0.2, #addition
      2 * 0.1, #multiplication
      2 * 0.2) #multiplication

# wrapping integers in str() for int --> str conversion
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# Try It Yourself
# 2-8 Operations to generate number 8
print(2 + 6,
      12 - 4,
      2 * 4,
      16 / 2)

# 2-9 Create and print favorite number in message
favorite_number = 4
message = "my favorite number is "+str(favorite_number) + ", but many poeple think otherwise."
print(message)

# Using comments begins with #
# Example:
# Say hello to everyone.
print("Hello Python people!")

import this # The Zen of Python, by Tim Peters
# This is a collection of guiding principles for writing computer programs in the Python language.
