import pytest

from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle


def test_not_valid_triangle():
    with pytest.raises(Exception):
        Triangle(a=6, b=6, c=0)


def test_not_valid_circle():
    with pytest.raises(Exception):
        Circle(radius=0)


def test_not_valid_square():
    with pytest.raises(Exception):
        Square(height=0)


def test_not_valid_rectangle():
    with pytest.raises(Exception):
        Rectangle(height=6, width=0)
