def count_digits(n):
    """This function count and return the number of digits of n"""
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print(count_digits(m))
