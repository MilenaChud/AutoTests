import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
import requests
import os
from selenium import webdriver



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


"""
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
"""


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="The browser for tests"
    )
    parser.addoption("--url", action="store", default="http://192.168.0.8:8081", help="reference on the web-site"
                     )
    parser.addoption("--drivers", action="store_true", default=os.path.expanduser("~/Desktop/Drivers"), help="path to drivers")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def run_browser(request):
    browser = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{drivers_folder}/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{drivers_folder}/geckodriver.exe")
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path=f"{drivers_folder}/yandexdriver.exe")
    else:
        raise ValueError("This browser doesn't exists")

    yield driver
    driver.close()
