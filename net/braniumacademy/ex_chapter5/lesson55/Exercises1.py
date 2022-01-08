import math


class Triangle:
    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def show_info(self):
        print(f'Triangle[a={self.a}, b={self.b}, c={self.c}]')

    def __add__(self, other):
        result = Triangle()
        result.a = self.a + other.a
        result.b = self.b + other.b
        result.c = self.c + other.c
        return result

    def __sub__(self, other):
        if self.a > other.a and self.b > other.b and self.c > other.c:
            result = Triangle()
            result.a = self.a - other.a
            result.b = self.b - other.b
            result.c = self.c - other.c
            return result
        else:
            print('Không trừ được vì cạnh của tam giác t1 nhỏ hơn cạnh tam giác t2.')
            return None

    def __str__(self):
        return f'Triangle[a={self.a}, b={self.b}, c={self.c}]'


def create_triangle(ith, obj):
    str1, str2, str3 = input(f'Nhập vào 3 cạnh của tam giác thứ {ith}: ').split()
    a = float(str1)
    b = float(str2)
    c = float(str3)
    if a + b > c and a + c > b and b + c > a:
        obj.a = a
        obj.b = b
        obj.c = c
    else:
        print(f'Ba giá trị bạn vừa nhập không phải 3 cạnh của tam giác.')


if __name__ == '__main__':
    option = '================== OPTION ==================\n' \
             '1. Nhập vào thông tin 2 tam giác.\n' \
             '2. Tính và hiển thị tổng 2 tam giác.\n' \
             '3. Tính và hiển thị hiệu 2 tam giác.\n' \
             '4. Tính và hiển thị chu vi tam giác tổng.\n' \
             '5. Tính và hiển thị chu vi tam giác hiệu.\n' \
             '6. Tính và hiển thị diện tích của tam giác tổng.\n' \
             '7. Tính và hiển thị diện tích của tam giác hiệu.\n' \
             '8. Kết thúc chương trình.\n' \
             'Xin mời chọn: '
    t1 = Triangle()
    t2 = Triangle()
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                create_triangle(1, t1)
                create_triangle(2, t2)
            case 2:
                print(f'{t1} + {t2} = {t1 + t2}')
            case 3:
                print(f'{t1} - {t2} = {t1 - t2}')
            case 4:
                print(f'Chu vi tam giác tổng: {(t1 + t2).calculate_perimeter()}')
            case 5:
                diff = t1 - t2
                if diff is not None:
                    print(f'Chu vi tam giác hiệu: {diff.calculate_perimeter()}')
            case 6:
                print(f'Diện tích tam giác tổng: {(t1 + t2).calculate_area()}')
            case 7:
                diff = t1 - t2
                if diff is not None:
                    print(f'Diện tích tam giác hiệu: {diff.calculate_area()}')
            case 8:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Sai chức năng. Vui lòng chọn lại! <==')
