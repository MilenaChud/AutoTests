import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from jsonschema import validate
import requests


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


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="reference on the web-site"
    )
    parser.addoption(
        "--status_code", action="store", default=200, help="status code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
