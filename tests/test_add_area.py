import pytest


def test_add_area_circle_and_circle(default_circle, other_circle):
    expected = 392.69908169872417
    assert default_circle.add_area(other_circle) == expected


def test_add_area_circle_and_square(default_circle, default_square):
    expected = 414.1592653589793
    assert default_circle.add_area(default_square) == expected


def test_add_area_circle_and_rectangle(default_circle, default_rectangle):
    expected = 514.1592653589794
    assert default_circle.add_area(default_rectangle) == expected


def test_add_area_circle_and_triangle(default_circle, default_triangle):
    expected = 320.1592653589793
    assert default_circle.add_area(default_triangle) == expected


def test_add_area_square_and_square(default_square, other_square):
    expected = 125
    assert default_square.add_area(other_square) == expected


def test_add_area_square_and_circle(default_square, default_circle):
    expected = 414.1592653589793
    assert default_square.add_area(default_circle) == expected


def test_add_area_square_and_rectangle(default_square, default_rectangle):
    expected = 300
    assert default_square.add_area(default_rectangle) == expected


def test_add_area_square_and_triangle(default_square, default_triangle):
    expected = 106
    assert default_square.add_area(default_triangle) == expected


def test_add_area_rectangle_and_rectangle(default_rectangle, other_rectangle):
    expected = 250
    assert default_rectangle.add_area(other_rectangle) == expected


def test_add_area_rectangle_and_circle(default_rectangle, default_circle):
    expected = 514.1592653589794
    assert default_rectangle.add_area(default_circle) == expected


def test_add_area_rectangle_and_square(default_rectangle, default_square):
    expected = 300
    assert default_rectangle.add_area(default_square) == expected


def test_add_area_rectangle_and_triangle(default_rectangle, default_triangle):
    expected = 206
    assert default_rectangle.add_area(default_triangle) == expected


def test_add_area_triangle_and_triangle(default_triangle, other_triangle):
    expected = 30
    assert default_triangle.add_area(other_triangle) == expected


def test_add_area_triangle_and_circle(default_triangle, default_circle):
    expected = 320.1592653589793
    assert default_triangle.add_area(default_circle) == expected


def test_add_area_triangle_and_square(default_triangle, default_square):
    expected = 106
    assert default_triangle.add_area(default_square) == expected


def test_add_area_triangle_and_rectangle(default_triangle, default_rectangle):
    expected = 206
    assert default_triangle.add_area(default_rectangle) == expected

