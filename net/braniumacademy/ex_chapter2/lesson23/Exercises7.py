t = int(input())
for i in range(1, t + 1):
    n_str, k_str = input().split()
    n = int(n_str)
    k = int(k_str)
    print(f"Test {i}: ")
    if n < 0 or k <= 0:
        print("INVALID")
    else:
        for x in range(1, n + 1):
            if x % k == 0:
                print(f"{x} ", end="")
        print()  # in xuống dòng
