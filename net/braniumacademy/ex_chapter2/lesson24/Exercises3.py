n = int(input())
if n <= 0:
    print("INVALID")
else:
    i = 2
    while n > 1:
        if n % i == 0:
            print(f"{i} ", end="")
            n //= i
        else:
            i += 1
