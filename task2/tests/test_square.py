import pytest
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


def test_positive_test_square(area_sq):
    with pytest.raises(ValueError):
        area_sq(2)


def test_negative_test_square(area_sq):
    with pytest.raises(ValueError):
        area_sq(-1)


def test_perimeter_of_square():
    with pytest.raises(ValueError):
        square = Square(8)
        square.perimeter()


def test_add_area():
    with pytest.raises(ValueError):
        rectangle = Circle(8)
        square = Square(8)

        square.add_area(rectangle)
