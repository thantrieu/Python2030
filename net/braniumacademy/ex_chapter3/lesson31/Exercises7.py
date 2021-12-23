import math


def ceil(n):
    """This function return nearest integer greater than n"""
    return int(math.ceil(n))


def floor(n):
    """This function return nearest integer less than n"""
    return int(math.floor(n))


def absolute(n):
    """This function return absolute value of n"""
    if n < 0:
        return n * -1
    else:
        return n


# Test code
x = float(input("Enter a number: "))
print(f"Min integer value less than {x}: {floor(x)}")
print(f"Min integer value greater than {x}: {ceil(x)}")
print(f"Absolute value of {x}: {absolute(x)}")
