def is_reversible(m):
    """This function check whether or not n is reversible number"""
    if m < 0:
        m *= -1
    x = m
    r = 0
    while m > 0:
        r = r * 10 + m % 10
        m //= 10
    return r == x


def listed_reverse_numbers(array):
    """This function listed all reverse numbers in list"""
    for index in range(0, len(array)):
        if is_reversible(arr[index]):
            print(f"{arr[index]} ", end="")
    print()


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    else:
        print(f"Test {i}:")
        listed_reverse_numbers(arr)
