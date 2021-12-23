import math


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = (result.denominator // self.denominator) * self.numerator + \
                           other.numerator * (result.denominator // other.denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = (result.denominator // self.denominator) * self.numerator - \
                           other.numerator * (result.denominator // other.denominator)
        result.simplify()
        return result

    def simplify(self):
        g = math.gcd(self.numerator, self.denominator)
        self.denominator = self.denominator // g
        self.numerator = self.numerator // g

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


p1 = Fraction(5, 8)
p2 = Fraction(1, 4)
psum = p1 + p2
pdif = p1 - p2
print(f'{p1} + {p2} = {psum}')
print(f'{p1} - {p2} = {pdif}')
