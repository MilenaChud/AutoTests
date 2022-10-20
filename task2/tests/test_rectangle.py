import pytest
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle

def test_positive_test_rectangle(area_re):
    with pytest.raises(ValueError):
        area_re(2, 5)


def test_negative_test_rectangle(area_re):
    with pytest.raises(ValueError):
        area_re(-10, -30)


def test_perimeter_of_rectangle(area_re):
    with pytest.raises(ValueError):
        rectangle = Rectangle(3, 9)
        rectangle.perimeter()


def test_add_area():
    with pytest.raises(ValueError):
        rectangle = Rectangle(8)
        square = Square(8)

        rectangle.add_area(square)