#31triangle.py
for i in range(1, 8, 2):
    for j in range(i):
        print("*", end = "")
    print()
#32triangle.py
for i in range(1, 8, 2):
    for j in range(i):
        print("*", end="")
    print()

for i in range(5, 0, -2):   
    for j in range(i):
        print("*", end="")
    print()
#33triangle.py
for i in range(1, 8, 2):
    for j in range(int((7-i)/2)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()
