h = int(input())
for i in range(1, h + 1):
    for j in range(1, 2 * h):
        if h - i + 1 <= j <= h + i - 1:
            print(f" {i - abs(h - j)} ", end="")
        else:
            print("   ", end="")
    print()
