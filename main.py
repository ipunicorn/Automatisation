from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

if __name__ == '__main__':
    new_rectangle = Rectangle(1, 2)
    new_square = Square(0)
    new_triangle = Triangle(5, 3, 4)

    print(new_square.perimeter())
