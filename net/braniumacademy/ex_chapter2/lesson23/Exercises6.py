t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n <= 0 or n > 20:
        print("INVALID")
    else:
        s = 0
        f = 1
        print(f"Test {i}: ")
        for x in range(1, n + 1):
            f *= x  # tìm x!
            s += f  # cộng x! vào tổng
        print(s)  # in xuống dòng
