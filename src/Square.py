from src.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Square'

    def __init__(self, height):
        self.height = height
        self.width = height
