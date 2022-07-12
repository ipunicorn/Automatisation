from src.Rectangle import Rectangle
from src.Square import Square

if __name__ == '__main__':
    new_rectangle = Rectangle(1, 2)
    new_square = Square(2)

    print(new_square.add_area(new_rectangle))
