t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}: ")
    if n <= 0:
        print("INVALID")
    else:
        s = 0
        for x in range(1, n + 1):
            s += x
        print(s)  # in xuống dòng
