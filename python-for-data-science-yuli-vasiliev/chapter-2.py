## python data structures
from collections import deque

"""
data structures organize and store data.
python has 4  data structures:
lists, tuples, dictionaries, and sets.
"""

# list
"""
list is an ordered collection of objects.
they are separated by commas.
the entire list is enclosed in square brackets.
lists are mutable, you can add, remove, and modify elements.
"""

example_1 = [2, 4, 7]
example_2 = ['Bob', 'John', 'Will']

# list allows different data types to be in one list
example_3 = ['Ford', 'America', 'Europe']

# creating a list
regions = ['Asia', 'America', 'Europe']
# list are usually populated by with a loop starting with an empty list
regions = []

# using common objects methods
my_list = []

# .append() to add items
my_list.append('Pay bills')
my_list.append('Tidy up')
my_list.append('Walk the dog')
my_list.append('Cook dinner')

# output
print(my_list)
print(my_list[0]) # for first element since python uses zero indexing

# inserting an item in between two items
i = my_list.index('Cook dinner')
my_list.insert(i, 'Go to the pharmacy')
print(my_list)

# to check how many times an item appears
print(my_list.count('Tidy up'))

# using slice notation
print(my_list[0:3])

# both start and end indices are optional
print(my_list[:3]) # omitting first
print(my_list[3:]) # omitting last
print(my_list[:]) # omitting both

# using slice notation for appending and inserting
my_list[len(my_list):] = ['Mow the lawn', 'Water plants']
# len returns the number of items in the list
print(my_list)

# Using a list as a queue
"""
a queue is an abstract data type.
one end for inserting items - enqueue, one end for removing items - dequeue
that is, first-in, first-out (FIFO)
"""

# turning a list to a queue using python's deque (double-ended queue) object
# using a to-do list example

# from collections import deque (move to the top)
queue = deque(my_list)
queue.append('Wash the car')
print(queue.popleft(), ' - Done!')
my_list_upd = list(queue)

# using a list as a stack
"""
a stack is an abstract data structure.
stack implements last-in, first-out (LIFO)
"""
my_list = ['Pay bills', 'Tidy up', 'Walk the dog', 'Go to the pharmacy', 'Cook dinner']
stack = []
for task in my_list:
    stack.append(task)
while stack:
    print(stack.pop(), ' - Done!')

# using lists and stacks for natural language processing
