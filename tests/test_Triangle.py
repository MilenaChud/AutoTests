import pytest
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


def test_positive_test_triangle(area_tr):
    with pytest.raises(ValueError):
        area_tr(10, 8, 11)



def test_negative_test_triangle(area_tr):
    with pytest.raises(ValueError):
        area_tr(0,-1, 3)



def test_perimeter_of_triangle():
    with pytest.raises(ValueError):
        triangle = Triangle(2, 8, 9)
        triangle.perimeter()


def test_add_area_positive():
    with pytest.raises(ValueError):
        triangle = Triangle(2, 5, 8)
        square = Square(8)

        triangle.add_area(square)