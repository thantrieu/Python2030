def reverse_number(n):
    """This function return reverse value of n"""
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + reverse_number(n // 10)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print(reverse_number(m))
