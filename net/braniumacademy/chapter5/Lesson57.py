import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @abstractmethod
    def calculate_area(self):
        """This method calculate shape's area."""
        pass

    @abstractmethod
    def calculate_perimeter(self):
        """This method calculate shape's perimeter."""
        pass


class Rectangle(Shape):
    def __init__(self, x=0, y=0, width=0, height=0):
        super(Rectangle, self).__init__(x, y)
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        return f'Rectangle[width={self.__width}, height={self.__height}, ' \
               f'area={self.calculate_area()}, ' \
               f'perimeter={self.calculate_perimeter()}]'


rect = Rectangle(width=20, height=30)
print(rect)


class AbstractCircle(Shape):
    def __init__(self, x=0, y=0, r=0):
        super(AbstractCircle, self).__init__(x, y)
        self.__radius = r

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f'AbstractCircle[radius={self.__radius}, area={self.calculate_area()}]'


circle = AbstractCircle(r=50)
print(circle)
