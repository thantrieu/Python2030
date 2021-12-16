import math

# Hằng số
F0 = 0
F1 = 1


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


if __name__ == '__main__':
    import sys

    num = int(sys.argv[1])
    print(f'{num} is prime number? {is_prime(num)}')
