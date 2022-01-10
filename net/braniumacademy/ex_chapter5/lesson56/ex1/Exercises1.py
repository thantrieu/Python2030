import math


class Shape:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def calculate_perimeter(self):
        """Phương thức tính chu vi của hình 2d."""
        return 0.0

    def calculate_area(self):
        """Phương thức tính diện tích của hình 2d."""
        return 0.0

    def show_info(self):
        print(f'Đây là hình 2d. Tọa độ tâm ({self.__x, self.__y})')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.__radius = radius

    def calculate_perimeter(self):
        """Phương thức tính chu vi của lớp cha được ghi đè lại trong lớp Circle."""
        return math.pi * 2 * self.__radius

    def calculate_area(self):
        """Phương thức tính diện tích của lớp cha được ghi đè lại trong lớp Circle."""
        return math.pi * self.__radius ** 2

    def show_info(self):
        print(f'Đây là hình Tròn. Tọa độ tâm ({self.__x, self.__y}), '
              f'bán kính r = {self.__radius}')


class Rectangle(Shape):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.__a = a
        self.__b = b

    def calculate_perimeter(self):
        """Phương thức tính chu vi của lớp cha được ghi đè lại trong lớp Rectangle."""
        return 2 * (self.__a + self.__b)

    def calculate_area(self):
        """Phương thức tính diện tích của lớp cha được ghi đè lại trong lớp Rectangle."""
        return self.__a * self.__b

    def show_info(self):
        print(f'Đây là hình Chữ nhật. Tọa độ tâm ({self.__x, self.__y}), '
              f'cạnh a = {self.__a}, b = {self.__b}')


class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.__a = a
        self.__b = b
        self.__c = c

    def calculate_perimeter(self):
        """Phương thức tính chu vi của lớp cha được ghi đè lại trong lớp Triangle."""
        return self.__a + self.__b + self.__c

    def calculate_area(self):
        """Phương thức tính diện tích của lớp cha được ghi đè lại trong lớp Triangle."""
        p = 0.5 * (self.__a + self.__b + self.__c)
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    def show_info(self):
        print(f'Đây là hình Tam giác. Tọa độ tâm ({self.__x, self.__y}), '
              f'Cạnh a = {self.__a}, b = {self.__b}, c = {self.__c}')


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
