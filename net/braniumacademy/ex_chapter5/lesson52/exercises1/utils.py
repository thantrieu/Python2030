import copy
import math

from net.braniumacademy.ex_chapter5.lesson52.exercises1.fraction import Fraction


def add_list_fractions(fractions):
    """Hàm tính tổng các phân số"""
    if len(fractions) > 0:
        copylist = copy.deepcopy(fractions)
        result = copylist[0]
        for i in range(1, len(fractions)):
            x = fractions[i]
            if x.denominator == result.denominator:
                result.numerator = result.numerator + x.numerator
            else:
                deno = math.lcm(result.denominator, x.denominator)
                result.numerator = deno // x.denominator * x.numerator + \
                                   result.numerator * deno // result.denominator
                result.denominator = deno
        result.simplify()
        return result
    else:
        return None


def multiply_list_fractions(fractions):
    """Hàm nhân các phân số trong danh sách"""
    if len(fractions) == 0:
        return None
    result = Fraction(1, 1)
    for x in fractions:
        result.denominator = result.denominator * x.denominator
        result.numerator = result.numerator * x.numerator
    result.simplify()
    return result


def display_fractions(fractions):
    """Hàm hiển thị danh sách phân số"""
    if len(fractions) > 0:
        for f in fractions:
            print(f'{f}, ', end='')
        print()
    else:
        print("==> Danh sách rỗng <==")


def create_fraction():
    """Hàm tạo và trả về phân số nếu thành công hoặc trả về None nếu không tạo được"""
    a, b = input("Nhập vào một phân số dạng a/b: ").split('/')
    if b == "0" or b == "0":
        print("Phân số không hợp lệ. Vui lòng nhập tử hoặc mẫu số khác 0.")
        return None
    else:
        return Fraction(int(a), int(b))
