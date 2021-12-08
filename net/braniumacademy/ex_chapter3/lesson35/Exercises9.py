import math

t = int(input())
for i in range(1, t + 1):
    a_str, b_str, c_str = input().split()
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    p = 0.5 * (a + b + c)
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Test {i}: {s:0.2f}")
