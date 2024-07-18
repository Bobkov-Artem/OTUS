"""Module Class abc Figure"""
from abc import ABC, abstractmethod


class Figure(ABC):
    """Class abc Figure"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_area(self):
        """method to calculate figure area"""

    @abstractmethod
    def get_perimeter(self):
        """method to calculate figure perimeter"""

    def add_area(self, other_figure):
        """method to calculate the area of two figures"""
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
