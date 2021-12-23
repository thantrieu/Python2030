n = int(input())
if n <= 0:
    print("INVALID")
else:
    i = 2
    count = 0
    while n > 1:
        if n % i == 0:
            count += 1
            n //= i
        else:
            if count > 0:
                print(f"{i}", end="")
                if count > 1:
                    print(f"^{count}", end="")
                if i != n // i:
                    print("x", end="")
            i += 1
            count = 0
    print(f"{i}", end="")
    if count > 1:
        print(f"^{count}")
