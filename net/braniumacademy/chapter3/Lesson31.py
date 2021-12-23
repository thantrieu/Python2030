def listed_divisible_by_k(n, k):
    """This function listed all numbers divisible by k"""
    if k == 0:
        print("k must be different from 0")
    else:
        for x in range(1, n + 1, 1):
            if x % k == 0:
                print(f"{x} ", end="")


listed_divisible_by_k(12, 4)
import math


def is_prime(n):
    """This function check whether or not n is prime number"""
    if n < 2:
        return False
    bound = int(math.sqrt(n))
    for x in range(2, bound + 1, 1):
        if n % x == 0:
            return False
    return True


print(is_prime(-17))
print(is_prime(12))
print(is_prime(19))


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


print(f"1 + 5 = {add(1, 5)}")
print(f"1 - 5 = {sub(1, 5)}")
print(f"1 * 5 = {mul(1, 5)}")
