from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'
    height = None
    width = None

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)
