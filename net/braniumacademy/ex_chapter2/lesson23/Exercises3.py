t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n <= 0:
        print("INVALID")
    else:
        s = 0
        print(f"Test {i}: ")
        for x in range(1, n + 1):
            s += x
        print(s)  # in xuống dòng
