import math


def is_prime(m):
    """This function check whether or not n is prime number"""
    if m < 2:
        return False
    bound = int(math.sqrt(m))
    for x in range(2, bound + 1):
        if m % x == 0:
            return False
    return True


def listed_primes(array):
    """This function listed all prime numbers in list"""
    for index in range(0, len(array)):
        if is_prime(arr[index]):
            print(f"({index}, {arr[index]}) ", end="")
    print()


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    else:
        print(f"Test {i}:")
        listed_primes(arr)
