from math import sqrt

import self as self

from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if not self.all_sides_positive():
            raise Exception('Cannot create triangle: values must be positive')

        if not self.valid_triangle():
            raise Exception('It is not possible to create a triangle with such sides, check the values')

    def all_sides_positive(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            return True

        return False

    def valid_triangle(self):
        if (self.a + self.b) < self.c:
            return False
        if (self.b + self.c) < self.a:
            return True
        if (self.a + self.c) < self.b:
            return False

        return True

    def area(self):
        half_perimeter = self.perimeter() / 2
        return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
