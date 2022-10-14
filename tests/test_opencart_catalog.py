from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main(run_browser, base_url):
    wait = WebDriverWait(run_browser, 10)
    run_browser.get(base_url)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    run_browser.find_element(By.CSS_SELECTOR, "button[type='button']")
    run_browser.find_element(By.NAME, "search")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-header")))
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))


def test_check_card_product(run_browser, base_url):
    wait = WebDriverWait(run_browser, 10)
    run_browser.get(base_url + "/camera/canon-eos-5d")
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Cameras')))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "thumbnail")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Description')))
    wait.until(EC.visibility_of_element_located((By.ID, "tab-description")))
    run_browser.find_element(By.CSS_SELECTOR, "button[type='button']")


def test_login_in_admin(run_browser, base_url):
    wait = WebDriverWait(run_browser, 10)
    run_browser.get(base_url + "/admin")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-title')))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@for='input-username']")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgotten Password')))
    run_browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    wait.until(EC.visibility_of_element_located((By.NAME, "password")))


def test_register_account(run_browser, base_url):
    wait = WebDriverWait(run_browser, 10)
    run_browser.get(base_url + "/index.php?route=account/register")
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "legend")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//label[@class='col-sm-2 control-label'][@for='input-firstname']")))
    run_browser.find_element(By.CLASS_NAME, 'col-sm-10')
    wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='submit'][@value='Continue']")))


def test_catalog(run_browser, base_url):
    wait = WebDriverWait(run_browser, 10)
    run_browser.get(base_url)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-toggle")))
    run_browser.find_element(By.CLASS_NAME, "see-all")
    run_browser.find_element(By.ID, "category")
    run_browser.find_element(By.CSS_SELECTOR, "button[type='button']")
    wait.until(EC.visibility_of_element_located((By.ID, "menu")))


