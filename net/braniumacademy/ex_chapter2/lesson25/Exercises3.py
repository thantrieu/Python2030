import math

t = int(input())
for i in range(1, t + 1):
    a_str, b_str, n_str = input().split()
    a = int(a_str)
    b = int(b_str)
    n = int(n_str)
    if a < 0 or b < 0 or a > b or n <= 0:
        print("NOT AVAILABLE")
    else:
        count = 0  # đếm số giá trị đã in ra
        for x in range(a, b + 1):
            bound = int(math.sqrt(x))
            if count < n and bound ** 2 == x:
                print(f"{x} ", end="")
                count += 1
            elif count >= n:
                break
        conclusion = ""
        if count == 0:
            conclusion = "NOT AVAILABLE"
        print(conclusion)
