import math
from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        if radius <= 0:
            raise Exception('Cannot create circle: radius must be positive')

        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
