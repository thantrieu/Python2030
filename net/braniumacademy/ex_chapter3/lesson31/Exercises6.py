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


def next_prime_number(n):
    """This function find and return next prime number"""
    if n < 2:
        return 2
    else:
        while True:
            if is_prime(n):
                return n
            else:
                n += 1


def previous_prime_number(n):
    """This function find and return previous prime number"""
    if n <= 2:
        return -1
    else:
        while True:
            if is_prime(n):
                return n
            else:
                n -= 1


def factorize_primes(n):
    """This function factorize n into prime factors"""
    i = 2
    while n > 1:
        if n % i == 0:
            print(f"{i}", end="")
            if n != i:
                print("x", end="")
            n //= i
        else:
            i += 1
    print()


def factorize_primes2(n):
    """This function factor n into primes factors in form t^k x y^m"""
    i = 2
    count = 0
    while n > 1:
        if n % i == 0:
            count += 1
            n //= i
        else:
            if count > 0:
                print(f"{i}", end="")
                if count > 1:
                    print(f"^{count}", end="")
                if i != n // i:
                    print("x", end="")
            i += 1
            count = 0
    print(f"{i}", end="")
    if count > 1:
        print(f"^{count}")
    print()


number = int(input("Enter an integer number: "))
print(f"Next prime number: {next_prime_number(number)}")
result = previous_prime_number(number)
print(f"Previous prime number: {'NOT AVAILABLE' if result < 0 else result}")
print("Factor n into prime factors: ")
factorize_primes(number)
print("Factor n into prime factors v2: ")
factorize_primes2(number)
