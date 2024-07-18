"""Module class Rectangle"""
from figure import Figure


class Rectangle(Figure):
    """Class Rectangle"""

    def __init__(self, side_a: int, side_b: int):
        """Initialization method"""
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника должны быть >0")
        self.__side_a = side_a
        self.__side_b = side_b

    def get_area(self):
        """method get_area"""
        area = self.__side_a * self.__side_b
        return area

    def get_perimeter(self):
        """method get_perimeter"""
        return 2 * (self.__side_a + self.__side_b)
