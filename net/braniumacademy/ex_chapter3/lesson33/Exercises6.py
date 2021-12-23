def first_digit(n):
    """This function find and return first digit of n"""
    if n < 10:
        return n
    else:
        return first_digit(n // 10)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print(first_digit(m))
