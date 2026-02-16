file_path = r'C:\Users\Dell\Documents\Projects\python-crash-course-eric-matthes\chapter_10\salem_horror.txt'


with open(file_path) as file_object:
    lines = file_object.readlines()

count = 0
for line in lines:
    count += line.lower().count('the')
print("There are " + str(count) + " instances of 'the' in the text")