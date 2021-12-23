def sum(n):
    if n == 1:
        return n
    else:
        return n + sum(n - 1)


m = int(input("Enter an integer number > 0: "))
print(f"S = {sum(m)}")
