import math

t = int(input())
for i in range(1, t + 1):
    n_str, k_str = input().split()
    n = int(n_str)
    k = int(k_str)
    if n < 0:
        print(f"Test {i}: ERROR")
    else:
        print(f"Test {i}: {round(math.sqrt(n), k)}")
