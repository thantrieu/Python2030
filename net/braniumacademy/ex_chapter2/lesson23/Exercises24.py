width = 7
height = 6
for i in range(1, height + 1):
    for j in range(1, width + 1):
        if (i == 1 and j != 1 and j != 4 and j != 7) or \
                (i == 2 or i == 3) or \
                (i == 4 and j != 1 and j != 7) or \
                (i == 5 and 3 <= j <= 5) or \
                (i == 6 and j == 4):
            print(" * ", end="")
        else:
            print("   ", end="")
    print()
