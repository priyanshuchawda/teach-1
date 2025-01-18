size = 5
for i in range(size):
    for j in range(size):
        if (i == 0 or i == size - 1) and (j == 0 or j == 1 or j == size - 2 or j == size - 1):
            print(1, end=" ")
        elif j == 2:
            print("*", end=" ")
        elif i == 2:
            print("*", end=" ")
        elif (i == 1 or i == size - 2) and (j == 0 or j == size - 1):
            print(1, end=" ")
        elif i == 1 or i == size - 2:
            print("*", end=" ")
        else:
            print("*", end=" ")
    print()