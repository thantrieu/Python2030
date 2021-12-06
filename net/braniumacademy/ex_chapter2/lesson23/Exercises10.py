t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n < 0:
        print(f"Test {i}:\nINVALID")
    else:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        print(f"Test {i}:\n{s}")
