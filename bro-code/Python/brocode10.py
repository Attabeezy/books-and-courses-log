#while loop = a statement that will execute code as long as condition remains true

#while 1==1:
#    print("Help! I'm stuck in a loop!")

#name = ""

#while len(name) == 0:
#    name = input("Enter your name: ")

#print(f"Hello {name}")

name = None

while not name:
    name = input("Enter your name: ")

print(f"Hello {name}")