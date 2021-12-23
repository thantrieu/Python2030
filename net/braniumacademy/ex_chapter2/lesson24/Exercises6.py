import math

n = int(input())
if n < 2:
    print("NO")
else:
    bound = int(math.sqrt(n))
    is_prime = True
    i = 2
    while i <= bound:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("YES")
    else:
        print("NO")
