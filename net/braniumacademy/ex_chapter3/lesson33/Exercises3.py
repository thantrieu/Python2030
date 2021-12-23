def sum_digits(n):
    """This function calculate and return sum of all digits of n"""
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print(sum_digits(m))
