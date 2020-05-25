import random

x = 'y'
print("This is a DICE SIMULATOR :")
while x == 'y':

    value = random.randint(1,6)

    if value == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    if value == 2:
        print("-----------")
        print("|         |")
        print("|  0   0  |")
        print("|         |")
        print("-----------")

    if value == 3:
        print("-----------")
        print("|    0    |")
        print("|    0    |")
        print("|    0    |")
        print("-----------")

    if value == 4:
        print("-----------")
        print("|  0   0  |")
        print("|         |")
        print("|  0   0  |")
        print("-----------")

    if value == 5:
        print("-----------")
        print("|  0   0  |")
        print("|    0    |")
        print("|  0   0  |")
        print("-----------")

    if value == 6:
        print("-----------")
        print("|  0   0  |")
        print("|  0   0  |")
        print("|  0   0  |")
        print("-----------")

    x = input("Press 'y' to roll again and any other key to exit:\n")
