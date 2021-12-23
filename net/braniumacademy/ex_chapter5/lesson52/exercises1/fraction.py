import math


class Fraction:
    """Lớp mô tả thông tin và hành động của phân số"""

    def __init__(self, numerator=0, denominator=1):
        """Hàm khởi tạo"""
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        """Hàm tính tổng hai phân số"""
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = \
            (result.denominator // self.denominator) * self.numerator + \
            other.numerator * (result.denominator // other.denominator)
        return result

    def sub(self, other):
        """Hàm tính hiệu hai phân số"""
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = \
            (result.denominator // self.denominator) * self.numerator - \
            other.numerator * (result.denominator // other.denominator)
        return result

    def mul(self, other):
        """Hàm tính tích hai phân số"""
        result = Fraction()
        result.denominator = self.denominator * other.denominator
        result.numerator = self.numerator * other.numerator
        return result

    def div(self, other):
        """Hàm tính thương hai phân số"""
        result = Fraction()
        result.denominator = self.denominator * other.numerator
        result.numerator = self.numerator * other.denominator
        return result

    def simplify(self):
        """Hàm rút gọn phân số"""
        g = math.gcd(self.numerator, self.denominator)  # Tìm ước chung
        self.denominator = self.denominator // g
        self.numerator = self.numerator // g

    def __str__(self):
        """Ghi đè phương thức to_string để hiển thị
        trực tiếp phân số trong hàm print()
        """
        return f'{self.numerator}/{self.denominator}'
