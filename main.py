from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

if __name__ == '__main__':
    new_rectangle = Rectangle(1, 1)
    new_square = Square(1)
    new_triangle = Triangle(1, 1, 1)

    print(new_square.add_area(new_rectangle))
