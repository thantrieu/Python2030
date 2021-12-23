t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}:")
    if n < 0:
        print("INVALID")
    else:
        prod = 0 if n == 0 else 1
        while n > 0:
            prod *= n % 10
            n //= 10
        print(prod)
