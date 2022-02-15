# Chỉ định kiểu của tham số, kiểu trả về của hàm
from math import sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    else:
        bound = int(sqrt(n))
        for i in range(2, bound + 1):
            if n % i == 0:
                return False
        return True


def get_full_name() -> str | None:
    name = input('Họ và tên: ')
    if len(name) > 0:
        return name
    else:
        return None


full_name = get_full_name()
if full_name is not None:
    print(full_name.upper())
