## Files and Exceptions

# Reading from a file (reading an entire file)
with open(r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
# 'r' makes python read string raw.

# Reading from a file (reading an entire file)
with open(r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# reading line by line
file_name = r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

# making a list of lines from a file
file_name = r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# working with a file's contents
file_name = r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

# 1 million pi's
file_path = r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_million_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line
print(pi_string[:52] + "...")
print(len(pi_string))

# is your birthday contained in Pi
file_path = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\pi_million_digits.txt"

with open(file_path) as file_object:
    lines = file_object.readlines()


pi_string= ''
for line in lines:
    pi_string += line.rstrip()

#birthday = input("Enter your birthday, in the form mmddyy")
birthday = '2394'
if birthday in pi_string:
    print("Your birthday appears in the digits of pi")
else:
    print("Your birthday doesn't appear in the digits of pi.")

# try it yourself
# 10-1 Learning Python
file_path = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\learning_python.txt"

# reading entire file
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# reading by looping over object
with open(file_path) as file_object:
    for line in file_object:
        print(line)

# reading by storing in a list and working outside
with open(file_path) as file_object:
    lines = file_object.readlines()
content = ''

for line in lines:
    content += line.rstrip()
    print(content)



# 10-2 Learning C
with open(file_path) as file_object:
    contents = file_object.readlines()

for line in contents:
    line = line.replace('Python', 'C')
    print(line)

file_path = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\programming.txt"

# writing lines to a file
with open(file_path, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

# appending to a file
with open(file_path, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# try it yourself
#10-3 Guest
#response = input("Name: ") #remove first '#' to make it interactive
response = 'Benjamin'

file_path = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\guest.txt"

with open(file_path, 'w') as file_object:
    file_object.write(response)

# 10-4 Guest Book
file_path = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\guest_book.txt"

key = True
while key:
    break
    response = input('Name: ')
    if response != "quit":
        with open(file_path, 'a') as file_object:
            file_object.write("\n" + response)
    else:
        key = False

# 10-5 Programming Poll

file_path = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\poll.txt"

while True:
    break
    name = input('What is your name? ')
    language = input('What Programming Language do you like? ')
    response = input(' Okay ' + name + ', why do you like ' + language + ' so much?')
    
    if response != "quit":
        with open(file_path, 'a') as file_object:
            file_object.write("\n" + response)
    else:
        break

# Exceptions
# Python uses exceptions to handle errors
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't' divide by zero!")

# Using Exceptions to Prevent Crashes
# Simple calculator for only division case study
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True:
    break # remove break to make code work!
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("You can only use numbers!")
    else:
        print(answer)

def count_words(file_path):
    """count the approx number of words in a file"""
    try:
        with open(file_path) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        #msg = "Sorry, the file " + file_path + " does not exist."
        #print(msg)
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print("The file " + file_path + " has about " + str(num_words) + " words.")

# analyzing text
title = "Alice in Wonderland"
print(title.split())

# working with multiple files
file_1 = r'alice.txt'
file_2 = r'little_women.txt'
file_3 = r'moby_dick.txt'
file_4 = r'siddhartha.txt'


file_paths = [file_1, file_2, file_3, file_4]

for file_path in file_paths:
    count_words(file_path)

# try it yourself
# 10-6 Addition
first = input('first number: ')
second = input('second number: ')
try:
    print(int(first) + int(second))
except TypeError:
    print("Enter numbers, please")

# 10-7 Addition Calculator
result = 0
while True:
    print("Enter a number or 'q' to exit")
    number = input('number: ')
    if number != 'q':
        result += int(number)
    else:
        break

# 10-8 Cats and Dogs
file_1 = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\cats.txt"
file_2 = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\dogs.txt"
file_3 = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_9\cats.txt"
file_4 = r"C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_9\dogs.txt"
"""
file 1 & 2 for true location testing
and
file 3 & 4 for false location testing
"""

try:
    with open(file_1) as file_object_1:
        for line in file_object_1:
            print(line.rstrip())
    
    with open(file_2) as file_object_2:
        for line in file_object_2:
            print(line.rstrip())
except FileNotFoundError:
    print("one or more files can't be found")

# 10-9 Silent Cats and Dogs
try:
    with open(file_1) as file_object_1:
        for line in file_object_1:
            print(line.rstrip())
    
    with open(file_2) as file_object_2:
        for line in file_object_2:
            print(line.rstrip())
except FileNotFoundError:
    pass

# 10-10 Common Words
file_path = r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\salem_horror.txt'


with open(file_path) as file_object:
    lines = file_object.readlines()

count = 0
for line in lines:
    count += line.lower().count('the')
print("There are " + str(count) + " instances of 'the' in the text")
