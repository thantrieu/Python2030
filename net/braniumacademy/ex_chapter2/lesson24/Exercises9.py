n = int(input())
if n <= 0:
    print("INVALID")
else:
    i = 1
    s = 0
    while i <= n:
        s += 1 / (i ** 3)
        i += 1
    print("{0:.6f}".format(s))
