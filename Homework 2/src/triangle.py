"""Module class Triangle"""
from figure import Figure
import math


class Triangle(Figure):
    name = "Class Triangle"

    def __init__(self, side_a, side_b, side_c):
        """Initialization method"""
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        if not all(isinstance(side, (float, int)) for side in [side_a, side_b, side_c]):

            raise TypeError(
                "стороны треугольника должны быть типа float или int")
        elif (side_a or side_b or side_c) <= 0:
            raise AssertionError("значение должно быть больше 0")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("передан не треугольник")

    def get_area(self):
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        area = math.sqrt(p * (p - self.__side_a) *
                         (p - self.__side_b) * (p - self.__side_c))
        return round(area, 2)

    def get_perimeter(self):
        perimeter = self.__side_a + self.__side_b + self.__side_c
        return perimeter
