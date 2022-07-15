import math
from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        self.radius = radius

        if not self.radius_positive():
            raise Exception('Cannot create circle: radius must be positive')

    def radius_positive(self):
        if self.radius > 0:
            return True

        return False

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
