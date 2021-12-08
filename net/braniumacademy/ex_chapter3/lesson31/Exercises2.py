def my_gcd(x, y):
    """This function find and return greatest common divisor of a and b"""
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def my_lcm(x, y):
    """This function find and return less common multiples of a and b"""
    return x * y // my_gcd(x, y)


a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)
print(f"UCLN = {my_gcd(a, b)}")
print(f"BCNN = {my_lcm(a, b)}")
