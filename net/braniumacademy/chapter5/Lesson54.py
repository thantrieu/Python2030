import math


class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calculate_perimeter(self):
        return 0.0

    def calculate_area(self):
        return 0.0


class Circle(Shape):
    def __init__(self, radius, x=0, y=0):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, x=0, y=0):
        super(Rectangle, self).__init__(x, y)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(20, 30)
circle = Circle(100)
print(f'Chu vi hình chữ nhật: {rect.calculate_perimeter()}')
print(f'Diện tích hình chữ nhật: {rect.calculate_area()}')
print(f'Chu vi hình tròn: {circle.calculate_perimeter()}')
print(f'Diện tích hình tròn: {circle.calculate_area()}')
