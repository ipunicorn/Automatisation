from math import sqrt
from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        half_perimeter = self.perimeter() / 2
        return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
