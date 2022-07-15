from src.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Square'

    def __init__(self, height):
        self.height = height
        self.width = height

        if not self.all_sides_positive():
            raise Exception('Cannot create square: all sides must be positive')

    def all_sides_positive(self):
        if self.height > 0:
            return True

        return False
