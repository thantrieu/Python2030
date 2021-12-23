n = int(input())
if n < 0:
    print("INVALID")
else:
    if n < 2:
        print(1)
    else:
        f = 1
        i = 2
        while i <= n:
            f *= i
            i += 1
        print(f)
