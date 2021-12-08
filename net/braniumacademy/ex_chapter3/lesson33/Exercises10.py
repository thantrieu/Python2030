def sum_sequence(n):
    """This function find and return sum from 1 to n"""
    if n <= 1:
        return n
    else:
        return 1 / n + sum_sequence(n - 1)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print("{0:0.3f}".format(sum_sequence(m)))
