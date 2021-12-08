def find_gcd(x, y):
    """This function return greates common divisor of x and y"""
    if y == 0:
        return x
    else:
        return find_gcd(y, x % y)


def find_lcm(x, y):
    """This function return less common multiples of x and y"""
    if x == 0 or y == 0:
        return "ERROR"
    else:
        return str(x * y // find_gcd(x, y))


t = int(input())
for i in range(1, t + 1):
    a_str, b_str = input().split()
    print(f"Test {i}: ")
    a = int(a_str)
    b = int(b_str)
    print(f"{find_gcd(a, b)} {find_lcm(a, b)}")
