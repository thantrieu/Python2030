t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n < 0:
        print("NO RESULT")
    else:
        print(f"Test {i}: ")
        for x in range(0, n + 1):
            if x % 2 == 0:
                print(f"{x} ", end="")
        print()  # in xuống dòng
