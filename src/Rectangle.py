from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'
    height = None
    width = None

    def __init__(self, height, width):
        if height <= 0 or width <= 0:
            raise Exception('Cannot create rectangle: all sides must be positive')

        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)
