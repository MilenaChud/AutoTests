import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.safari.options import Options
import pytest


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
    parser.addoption("--drivers", action="store_true", default=os.path.expanduser("~/Desktop/Drivers"),
                     help="path to drivers")
    parser.addoption("--executor", action="store", default="192.168.0.8", help="The web page of selenoid")
    parser.addoption("--bv")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def run_browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    browser_version = request.config.getoption("--bv")
    drivers_folder = request.config.getoption("--drivers")

    executor_url = "http://{}:4444/wd/hub".format(executor)

    caps = {
        "browserName": browser,
        "platformname": "WINDOWS",
        "browserVersion": browser_version,
        # "screenResolution": "1280x720",
    }

    options = Options()

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps,
        options=options
    )

    failed_before = request.session.testsfailed

    yield driver

    if request.session.testsfailed != failed_before:
        test_name = request.node.name
    take_screenshot(driver, test_name)

    driver.close()


"""
    driver = webdriver.Chrome(executable_path=f"{drivers_folder}/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{drivers_folder}/geckodriver.exe")
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path=f"{drivers_folder}/yandexdriver.exe")
    else:
        raise ValueError("This browser doesn't exists")
"""


def take_screenshot(driver, test_name):
    screenshot_file_path = "{}/{}.png".format("tests/logs/", test_name)
    driver.save_screenshot(screenshot_file_path)
