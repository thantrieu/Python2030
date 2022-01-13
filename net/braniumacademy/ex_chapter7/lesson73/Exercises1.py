import math


def is_prime(n):
    """Hàm kiểm tra số n có phải số nguyên tố hay không."""
    if n < 2:
        return False
    bound = int(math.sqrt(n))
    for i in range(2, bound):
        if n % i == 0:
            return False
    return True


def get_number():
    """Hàm nhận input và chuyển đổi sang số nguyên nếu có thể."""
    try:
        string = input('Nhập vào số nguyên n: ')
        if not string.isdigit():
            raise ValueError('Giá trị bạn nhập không phải số nguyên')
        else:
            return int(string)
    except ValueError as e:
        print(e)
        return None


if __name__ == '__main__':
    # nơi chạy chương trình
    number = get_number()
    if number is not None:
        print(f'{number} là số nguyên tố? {is_prime(number)}')
