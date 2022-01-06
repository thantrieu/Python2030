import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show_info(self):
        print(f'Đây là hình 2d. Tọa độ tâm ({self.x, self.y})')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def calculate_perimeter(self):
        return math.pi * 2 * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def calculate_perimeter(self):
        return 2 * (self.a + self.b)

    def calculate_area(self):
        return self.a * self.b


class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        p = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# Đoạn code chạy chương trình:
if __name__ == '__main__':
    print('==> Hình 2d:')
    shape = Shape(10, 58)  # tạo đối tượng shape
    shape.show_info()

    print('==> Hình tròn: ')
    circle = Circle(0, 0, 25.25)  # tạo đối tượng circle
    print(f'Chu vi: {circle.calculate_perimeter()}')
    print(f'Diện tích: {circle.calculate_area()}')

    print('==> Hình tam giác: ')
    triangle = Triangle(0, 0, 30, 40, 50)  # tạo đối tượng triangle
    print(f'Chu vi: {triangle.calculate_perimeter()}')
    print(f'Diện tích: {triangle.calculate_area()}')

    print('==> Hình chữ nhật: ')
    rect = Rectangle(0, 0, 30, 25)  # tạo đối tượng rectangle
    print(f'Chu vi: {rect.calculate_perimeter()}')
    print(f'Diện tích: {rect.calculate_area()}')
