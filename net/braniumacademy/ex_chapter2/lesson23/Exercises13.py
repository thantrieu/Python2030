t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}:")
    if n <= 0:
        print("INVALID")
    else:
        for x in range(1, n + 1):
            if n % x == 0:
                print(f"{x} ", end="")
        print()  # in ra dòng trống
