from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

    def find_of_element_id(self, id_):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, id_)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(id_))

    def find_of_element_name(self, name):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.NAME, name)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(name))

    def find_of_element_class_name(self, class_name):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(class_name))

    def find_of_element_tag(self, tag):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.TAG_NAME, tag)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(tag))

    def find_of_element_link(self, link):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, link)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(link))

    def find_of_element_css(self, link):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, link)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(link))

    def find_of_element_path(self, path):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, path)))
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(path))

    def find_button(self, type_of_button):
        return self.browser.find_element(By.CSS_SELECTOR, "button[type='{}']".format(type_of_button))

    def click(self, element):
        ActionChains(self.browser).move_to_element(element).pause(0.5).click().perform()

    def input(self, element, data):
        try:
            point = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.NAME, element)))
            self.click(point)
            point.clear()
            point.send_keys(data)
        except TimeoutException:
            raise AssertionError("Элемент не успел загрузиться {}".format(element))