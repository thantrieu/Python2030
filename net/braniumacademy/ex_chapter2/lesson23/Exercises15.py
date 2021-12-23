import math

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}: ", end="")
    if n <= 1:
        print("NO")
    else:
        s = 1  # tổng ước nhỏ hơn n
        bound = int(math.sqrt(n))
        for x in range(2, bound + 1):
            if n % x == 0:  # nếu x là ước của n
                s += x
                if n // x != x:
                    s += n // x
        if s == n:
            print("YES")
        else:
            print("NO")
