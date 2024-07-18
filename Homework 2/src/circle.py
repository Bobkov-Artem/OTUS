"""Module class Circle"""
from figure import Figure
import math


class Circle(Figure):
    name = "Class Circle"

    def __init__(self, radius):
        """Initialization method"""
        self.__radius = radius
        if not isinstance(radius, (float, int)):
            raise TypeError("Радиус должен быть типа float или int")
        elif radius <= 0:
            raise AssertionError("Радиус должен быть больше 0")

    def get_area(self):
        area = math.pi * (self.__radius ** 2)
        return round(area, 2)

    def get_perimeter(self):
        circumference = 2 * math.pi * self.__radius
        return round(circumference, 2)
