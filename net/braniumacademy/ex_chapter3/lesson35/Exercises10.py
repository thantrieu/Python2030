import math

t = int(input())
for i in range(1, t + 1):
    c = float(input())  # cạnh huyền
    a = c * math.sin(math.radians(35))  # độ dài cạnh a
    b = c * math.cos(math.radians(35))  # độ dài cạnh b
    s = 0.5 * a * b  # diện tích
    p = a + b + c  # chu vi
    print(f"Test {i}: {a:0.3f} {b:0.3f} {p:0.3f} {s:0.3f}")
