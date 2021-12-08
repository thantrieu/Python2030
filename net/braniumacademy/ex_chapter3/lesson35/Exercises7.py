import random

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}: {int(n * random.random())}")
