h = int(input())
for i in range(1, h + 1):
    for j in range(1, 2 * h):
        if j == h - i + 1 or i == h or j == h + i - 1:
            print(" 1 ", end="")
        else:
            print("   ", end="")
    print()
