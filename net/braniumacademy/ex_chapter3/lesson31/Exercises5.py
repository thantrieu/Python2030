import math


def is_prime(n):
    """This function check whether or not n is prime number"""
    if n < 2:
        return False
    else:
        bound = int(math.sqrt(n))
        for x in range(2, bound + 1):
            if n % x == 0:
                return False
        return True


def listed_all_prime_numbers(a, b):
    """This function listed all prime numbers in range a to b"""
    for x in range(a, b + 1):
        if is_prime(x):
            print(f"{x} ", end="")
    print()


def is_square(n):
    """This function check whether or not n is square"""
    if n < 0:
        return False
    i = int(math.sqrt(n))
    return i ** 2 == n


def listed_all_square(a, b):
    """This function listed all square number in range a to b"""
    for x in range(a, b + 1):
        if is_square(x):
            print(f"{x} ", end="")
    print()


def is_reversible(n):
    """This function check whether or not n is reversible number"""
    if n < 0:
        n *= -1
    f = n
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return f == r


def listed_all_reverse(a, b):
    """This function listed all reverse number in range a to b"""
    for x in range(a, b + 1):
        if is_reversible(x):
            print(f"{x} ", end="")
    print()


def sum_digits(n):
    """This function return sum all digits of n"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def listed_all_sum_digits_is_prime(a, b):
    """This function listed all number x in range a to b
    that sum all digits of x is prime number"""
    for x in range(a, b + 1):
        if is_prime(sum_digits(x)):
            print(f"{x} ", end="")
    print()


a_str, b_str = input().split()
a_value = int(a_str)
b_value = int(b_str)
print("List of all prime numbers: ")
listed_all_prime_numbers(a_value, b_value)
print("List of all square numbers: ")
listed_all_square(a_value, b_value)
print("List of all reverse numbers: ")
listed_all_reverse(a_value, b_value)
print("List of all numbers have sum digits is prime: ")
listed_all_sum_digits_is_prime(a_value, b_value)
