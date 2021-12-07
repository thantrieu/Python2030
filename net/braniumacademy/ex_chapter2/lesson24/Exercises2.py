n = int(input())
if n <= 0:
    print("INVALID")
else:
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n //= 10
    print(s)
