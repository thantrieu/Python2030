t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}: ", end="")
    if n < 0:
        print("INVALID")
    else:
        f0 = 0
        f1 = 1
        fn = n
        for x in range(2, n + 1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        print(fn)
