#nested loop = loop in another loop
# inner loop will finish before one iteration of outer loop

rows = int(input("How many rows: "))
colomns = int(input("How many colomns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colomns):
        print(symbol, end="")
    print()