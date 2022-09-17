import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture
def default_circle():
    return Circle(radius=10)


@pytest.fixture
def default_square():
    return Square(height=10)


@pytest.fixture
def default_rectangle():
    return Rectangle(height=10, width=20)


@pytest.fixture
def default_triangle():
    return Triangle(a=3, b=4, c=5)


@pytest.fixture
def other_circle():
    return Circle(radius=5)


@pytest.fixture
def other_square():
    return Square(height=5)


@pytest.fixture
def other_rectangle():
    return Rectangle(height=5, width=10)


@pytest.fixture
def other_triangle():
    return Triangle(a=6, b=8, c=10)
