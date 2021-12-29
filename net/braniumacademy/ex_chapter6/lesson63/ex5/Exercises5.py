import math


def is_square(m):
    """This function check whether or not n is square number"""
    if m < 0:
        return False
    v = int(math.sqrt(m))
    return v * v == m  # if v^2 == m, m is square number


def listed_squares(array):
    """This function listed all square numbers in list"""
    for index in range(0, len(array)):
        if is_square(arr[index]):
            print(f"({index}, {arr[index]}) ", end="")
    print()


with open('input5.txt') as reader:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            print(f"Test {i}:\nN INVALID")
        else:
            print(f"Test {i}:")
            listed_squares(arr)
