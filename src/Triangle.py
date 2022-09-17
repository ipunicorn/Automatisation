from math import sqrt

import self as self

from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise Exception('Cannot create triangle: values must be positive')
        if (a + b) < c:
            raise Exception('It is not possible to create a triangle with such sides, check the values')
        if (b + c) < a:
            raise Exception('It is not possible to create a triangle with such sides, check the values')
        if (a + c) < b:
            raise Exception('It is not possible to create a triangle with such sides, check the values')

        self.a = a
        self.b = b
        self.c = c

        if not self.valid_triangle():
            raise Exception('It is not possible to create a triangle with such sides, check the values')

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
