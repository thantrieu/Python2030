import math

t = int(input())
for i in range(1, t + 1):
    r = float(input())
    print(f"Test {i}:\n{2 * math.pi * r:0.3f}\n{math.pi * r * r:0.3f}")
