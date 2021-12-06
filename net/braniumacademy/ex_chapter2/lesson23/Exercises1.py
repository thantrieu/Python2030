t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}: ")
    if n < 0:
        print("NO RESULT")
    else:
        for x in range(0, n + 1):
            if x % 2 == 0:
                print(f"{x} ", end="")
        print()  # in xuống dòng
