import pytest


def test_area_circle(default_circle):
    expected = 314.1592653589793
    assert default_circle.area() == expected


def test_area_rectangle(default_rectangle):
    expected = 200
    assert default_rectangle.area() == expected


def test_area_square(default_square):
    expected = 100
    assert default_square.area() == expected


def test_area_triangle(default_triangle):
    expected = 6
    assert default_triangle.area() == expected


