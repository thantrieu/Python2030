def add(x, y):
    """This function return sum of a and b"""
    return x + y


def sub(x, y):
    """This function return different of a and b"""
    return x - y


def mul(x, y):
    """This function return product of a and b"""
    return x * y


def div(x, y):
    """This function return division of a and b"""
    return x / y


def exp(x, y):
    """This function return exponent of a and b"""
    return x ** y


def div2(x, y):
    return x // y


a_str, b_str = input().split()
a = float(a_str)
b = float(b_str)
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
print(f"{a} // {b} = {div2(a, b)}")
print(f"{a} ** {b} = {exp(a, b)}")
