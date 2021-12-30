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


def listed_primes(mwriter, array):
    """This function listed all prime numbers in list"""
    for index in range(0, len(array)):
        if is_prime(arr[index]):
            mwriter.write(f"({index}, {arr[index]}) ")
    mwriter.write('\n')


with open('input4.txt') as reader, open('output4.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            writer.write(f"Test {i}:\nN INVALID\n")
        else:
            writer.write(f"Test {i}:\n")
            listed_primes(writer, arr)
