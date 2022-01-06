import math


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_perimeter(self):
        """Phương thức tính chu vi của hình 2d."""
        return 0.0

    def calculate_area(self):
        """Phương thức tính diện tích của hình 2d."""
        return 0.0

    def show_info(self):
        print(f'Đây là hình 2d. Tọa độ tâm ({self.x, self.y})')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def calculate_perimeter(self):
        """Phương thức tính chu vi của lớp cha được ghi đè lại trong lớp Circle."""
        return math.pi * 2 * self.radius

    def calculate_area(self):
        """Phương thức tính diện tích của lớp cha được ghi đè lại trong lớp Circle."""
        return math.pi * self.radius ** 2

    def show_info(self):
        print(f'Đây là hình Tròn. Tọa độ tâm ({self.x, self.y}), '
              f'bán kính r = {self.radius}')


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def calculate_perimeter(self):
        """Phương thức tính chu vi của lớp cha được ghi đè lại trong lớp Rectangle."""
        return 2 * (self.a + self.b)

    def calculate_area(self):
        """Phương thức tính diện tích của lớp cha được ghi đè lại trong lớp Rectangle."""
        return self.a * self.b

    def show_info(self):
        print(f'Đây là hình Chữ nhật. Tọa độ tâm ({self.x, self.y}), '
              f'cạnh a = {self.a}, b = {self.b}')


class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        """Phương thức tính chu vi của lớp cha được ghi đè lại trong lớp Triangle."""
        return self.a + self.b + self.c

    def calculate_area(self):
        """Phương thức tính diện tích của lớp cha được ghi đè lại trong lớp Triangle."""
        p = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def show_info(self):
        print(f'Đây là hình Tam giác. Tọa độ tâm ({self.x, self.y}), '
              f'Cạnh a = {self.a}, b = {self.b}, c = {self.c}')


# Đoạn code chạy chương trình:
if __name__ == '__main__':
    print('==> Hình 2d:')
    shape = Shape(10, 58)  # tạo đối tượng shape
    shape.show_info()

    print('==> Hình tròn: ')
    circle = Circle(0, 0, 25.25)  # tạo đối tượng circle
    print(f'Chu vi: {circle.calculate_perimeter()}')
    print(f'Diện tích: {circle.calculate_area()}')
    circle.show_info()

    print('==> Hình tam giác: ')
    triangle = Triangle(0, 0, 30, 40, 50)  # tạo đối tượng triangle
    print(f'Chu vi: {triangle.calculate_perimeter()}')
    print(f'Diện tích: {triangle.calculate_area()}')
    triangle.show_info()

    print('==> Hình chữ nhật: ')
    rect = Rectangle(0, 0, 30, 25)  # tạo đối tượng rectangle
    print(f'Chu vi: {rect.calculate_perimeter()}')
    print(f'Diện tích: {rect.calculate_area()}')
    rect.show_info()
