import pytest


def test_perimeter_circle(default_circle):
    expected = 62.83185307179586
    assert default_circle.perimeter() == expected


def test_perimeter_rectangle(default_rectangle):
    expected = 60
    assert default_rectangle.perimeter() == expected


def test_perimeter_square(default_square):
    expected = 40
    assert default_square.perimeter() == expected


def test_perimeter_triangle(default_triangle):
    expected = 12
    assert default_triangle.perimeter() == expected


