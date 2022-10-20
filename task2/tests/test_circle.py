import pytest
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


def test_positive_test_circle():
    with pytest.raises(ValueError):
        circle = Circle(2)
        circle.area()


def test_negative_test_circle():
    with pytest.raises(ValueError):
        circle = Circle(-1)
        circle.area()


def test_perimeter_of_circle():
    with pytest.raises(ValueError):
        circle = Circle(8)
        circle.perimeter()


def test_add_area_positive():
    with pytest.raises(ValueError):
        circle = Circle(8)
        square = Square(8)

        circle.add_area(square)
