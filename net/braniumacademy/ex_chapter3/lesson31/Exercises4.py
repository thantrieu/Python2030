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


def is_reverse_prime(n):
    """This function check whether or not reverse number of n is prime number"""
    if n < 2:
        return False
    else:
        r = 0
        while n > 0:
            r = r * 10 + n % 10
            n //= 10
        return is_prime(r)


def sum_digits(n):
    """This function return sum all digits of n"""
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def is_sum_all_digits_prime(n):
    """This function check whether or not sum of all digits of n is prime number"""
    s = sum_digits(n)
    return is_prime(s)


value = int(input("Enter an integer number: "))
print(f"{value} is prime number? {is_prime(value)}")
print(f"{value} is reversible number? {is_reversible(value)}")
print(f"Reversible value of {value} is prime valueumber? {is_prime(value)}")
print(f"Sum all digits of {value} is prime valueumber? {is_prime(value)}")
