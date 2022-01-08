import math


class Fraction:
    """Class describe info behavior of fraction."""

    def __init__(self, numerator=0, denominator=1):
        """This method initilize numerator and denominator of a fraction."""
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """This overload + operator to add two fractions and return fraction result."""
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = \
            (result.denominator // self.denominator) * self.numerator + \
            other.numerator * (result.denominator // other.denominator)
        return result

    def __sub__(self, other):
        """This overload - operator to subtract two fractions and return fraction result."""
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = \
            (result.denominator // self.denominator) * self.numerator - \
            other.numerator * (result.denominator // other.denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        """This function overloading operator to multiple two fractions."""
        result = Fraction()
        result.denominator = self.denominator * other.denominator
        result.numerator = self.numerator * other.numerator
        result.simplify()
        return result

    def __truediv__(self, other):
        """This function overloading operator to divide two fractions."""
        result = Fraction()
        result.denominator = self.denominator * other.numerator
        result.numerator = self.numerator * other.denominator
        result.simplify()
        return result

    def __eq__(self, other):
        """This overload operator compare two fractions equals or not."""
        self.simplify()
        other.simplify()
        return self.denominator == other.denominator and \
               self.numerator == other.numerator

    def __ne__(self, other):
        """This overload operator compare two fractions for not equals."""
        self.simplify()
        other.simplify()
        return self.numerator != other.numerator or \
               self.denominator != other.denominator

    def __gt__(self, other):
        self.simplify()
        other.simplify()
        return (self.numerator / self.denominator) > \
               (other.numerator / other.denominator)

    def __lt__(self, other):
        self.simplify()
        other.simplify()
        return (self.numerator / self.denominator) < \
               (other.numerator / other.denominator)

    def __ge__(self, other):
        self.simplify()
        other.simplify()
        return (self.numerator / self.denominator) >= \
               (other.numerator / other.denominator)

    def __le__(self, other):
        self.simplify()
        other.simplify()
        return (self.numerator / self.denominator) <= \
               (other.numerator / other.denominator)

    def simplify(self):
        """This method simplify denominator and numerator of current fraction."""
        g = math.gcd(self.numerator, self.denominator)  # Tìm ước chung
        self.denominator = self.denominator // g
        self.numerator = self.numerator // g

    def __str__(self):
        """This overloading method return infomation of a fraction."""
        return f"{self.numerator}/{self.denominator}"


def create_fractions(ith):
    str1, str2 = input(f'Nhập phân số thứ {ith}, dạng tử/mẫu: ').split('/')
    return Fraction(int(str1), int(str2))


if __name__ == '__main__':
    option = '================= MENU =================\n' \
             '1. Tổng 2 phân số.\n' \
             '2. Hiệu 2 phân số.\n' \
             '3. Tích 2 phân số.\n' \
             '4. Thương 2 phân số.\n' \
             '5. So sánh == hai phân số.\n' \
             '6. So sánh != hai phân số.\n' \
             '7. So sánh < hai phân số.\n' \
             '8. So sánh > hai phân số.\n' \
             '9. So sánh <= hai phân số.\n' \
             '10. So sánh >= hai phân số.\n' \
             '11. Thoát chương trình.\n' \
             'Xin mời chọn: '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} + {p2} = {p1 + p2}')
            case 2:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} - {p2} = {p1 - p2}')
            case 3:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                p3 = p1 * p2
                print(f'{p1} * {p2} = {p3}')
            case 4:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} / {p2} = {p1 / p2}')
            case 5:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} == {p2} ? {p1 == p2}')
            case 6:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} != {p2} ? {p1 != p2}')
            case 7:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} < {p2} ? {p1 < p2}')
            case 8:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} > {p2} ? {p1 > p2}')
            case 9:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} <= {p2} ? {p1 <= p2}')
            case 10:
                p1 = create_fractions(1)
                p2 = create_fractions(2)
                print(f'{p1} >= {p2} ? {p1 >= p2}')
            case 11:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Sai chức năng. Vui lòng chọn lại! <==')
