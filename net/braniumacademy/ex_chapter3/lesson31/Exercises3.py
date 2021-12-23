def sum_digits(m):
    """This function return sum all digits of n"""
    s = 0
    while m > 0:
        s += m % 10
        m //= 10
    return s


def mul_digits(m):
    """This function return product of all digits of n"""
    s = 1
    while m > 0:
        s *= m % 10
        m //= 10
    return s


def first_digit(m):
    """This function return first digit of a number"""
    while m > 10:
        m //= 10
    return m


n = int(input("Nhập số nguyên dương n: "))
print(f"Tổng các chữ số của {n}: {sum_digits(n)}")
print(f"Tích các chữ số của {n}: {mul_digits(n)}")
print(f"Chữ số đầu tiên của {n}: {first_digit(n)}")
