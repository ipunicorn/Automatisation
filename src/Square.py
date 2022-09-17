from src.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Square'

    def __init__(self, height):
        if height <= 0:
            raise Exception('Cannot create square: all sides must be positive')
        self.height = height
        self.width = height

