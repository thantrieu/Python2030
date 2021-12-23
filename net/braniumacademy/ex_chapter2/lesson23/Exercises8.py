import math

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        bound = int(math.sqrt(n))
        for x in range(2, bound + 1):
            if n % x == 0:
                is_prime = False
                break
    if is_prime is True:
        print(f"Test {i}: YES")
    else:
        print(f"Test {i}: NO")
