def fac(n):
    """This function find and return n!"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print(fac(m))
