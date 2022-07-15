from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'
    height = None
    width = None

    def __init__(self, height, width):
        self.height = height
        self.width = width

        if not self.all_sides_positive():
            raise Exception('Cannot create rectangle: all sides must be positive')

    def all_sides_positive(self):
        if self.height > 0 and self.width > 0:
            return True

        return False

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)
