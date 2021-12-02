import math


def is_prime(x):
    """This function check whether or not x is prime number"""
    if x < 2:
        return False
    bound = int(math.sqrt(x))
    for i in range(2, bound + 1):
        if x % i == 0:
            return False
    return True


first_name = "Nam"
age = 20
last_name = "Nguyen"
mid_name = "Van"

for x in range(10):
    print(x)
    for y in range(10):
        print(y)

# This code....
for x in range(10):
    print(x)
    for y in range(10):
        print(y)

for x in range(10):
    print(x)
    for y in range(10):
        print(y)

result = is_prime(2)
if result is True:
    print("OK")
else:
    print("NONONO")

a = 5 + 7 + 9 * 3 - 7
