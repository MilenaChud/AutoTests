import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle

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

