from Figure import Figure
from abc import ABC, abstractmethod


class Rectangle(Figure):
    @abstractmethod
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(' side_a and side_b must be positive integers')
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
