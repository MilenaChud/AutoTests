from task2.Triangle import Triangle
from task2.Square import Square
from task2.Circle import Circle
from task2.Rectangle import Rectangle
import pytest


@pytest.fixture
def area_tr(a, b, c):
    triangle = Triangle(a, b, c)
    return triangle.area()


@pytest.fixture
def area_sq(a):
    square = Square(a)
    return square.area()


@pytest.fixture
def area_ci(a):
    circle = Circle(a)
    return circle.area()


@pytest.fixture
def area_re(a, b):
    rectangle = Rectangle(a, b)
    return rectangle.area()
