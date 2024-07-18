"""Module class Square"""
from rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, side):
        """Initialization method"""
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть >0")
        super().__init__(side, side)
        self.name = __class__.__name__
