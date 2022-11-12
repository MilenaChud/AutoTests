from tests.page_object.WishList import WishList
from tests.page_object.BasePage import BasePage
from selenium.webdriver.common.by import By
from tests.page_object.Sign_up import SingUp
import allure


@allure.title("Test checks a main page")
def test_check_main(run_browser, base_url):
    main_page = BasePage(run_browser)
    main_page.open_page(base_url)
    main_page.find_of_element_id("logo")
    main_page.find_button("button")
    main_page.find_of_element_name("search")
    main_page.find_of_element_class_name("navbar-header")
    main_page.find_of_element_tag("h3")


@allure.title("Test checks a product card")
def test_check_card_product(run_browser, base_url):
    path = base_url + "/camera/canon-eos-5d"
    main_page = BasePage(run_browser)
    main_page.open_page(path)
    main_page.find_of_element_link('Cameras')
    main_page.find_of_element_class_name("thumbnail")
    main_page.find_of_element_link('Description')
    main_page.find_of_element_id("tab-description")
    main_page.find_button('button')


@allure.title("Test checks log in page")
def test_login_in_admin(run_browser, base_url):
    path = base_url + "/admin"
    main_page = BasePage(run_browser)
    main_page.open_page(path)
    main_page.find_of_element_class_name('panel-title')
    main_page.find_of_element_path("//label[@for='input-username']")
    main_page.find_of_element_link('Forgotten Password')
    main_page.find_button('submit')
    main_page.find_of_element_name("password")


@allure.title("Test checks an opportunity of registration on a page")
def test_register_account(run_browser, base_url):
    path = base_url + "/index.php?route=account/register"
    main_page = BasePage(run_browser)
    main_page.open_page(path)
    main_page.find_of_element_tag("legend")
    main_page.find_of_element_path("//label[@class='col-sm-2 control-label'][@for='input-firstname']")
    run_browser.find_element(By.CLASS_NAME, 'col-sm-10')
    main_page.find_of_element_name("password")
    main_page.find_of_element_path("//input[@type='submit'][@value='Continue']")


@allure.title("Test checks a catalog")
def test_catalog(run_browser, base_url):
    main_page = BasePage(run_browser)
    main_page.open_page(base_url)
    main_page.find_of_element_class_name("dropdown-toggle")
    run_browser.find_element(By.CLASS_NAME, "see-all")
    run_browser.find_element(By.ID, "category")
    main_page.find_button('button')
    main_page.find_of_element_id("menu")


@allure.title("Test checks a currency")
def test_currency(run_browser, base_url):
    main_page = BasePage(run_browser)
    main_page.open_page(base_url)
    button = main_page.find_of_element_path("//button[@data-toggle='dropdown']")
    main_page.click(button)
    cur_eu = main_page.find_of_element_name("EUR")
    main_page.click(cur_eu)


@allure.title("Test checks an opportunity of sign in")
def test_sign_up(run_browser, base_url):
    reg_page = SingUp(run_browser)
    reg_page.open_page(base_url)
    reg_page.open_register()
    reg_page.input_firstname()
    reg_page.input_lastname()
    reg_page.input_email()
    reg_page.input_telephone()
    reg_page.input_password()
    reg_page.input_confirm_password()
    reg_page.button_continue()


@allure.feature('Authorization')
@allure.story('Invalid credentials')
@allure.title("Test checks a wish list")
def test_add_wish_list(run_browser, base_url):
    wish_list = WishList(run_browser)
    wish_list.open_page(base_url)
    wish_list.open_catalog()
    wish_list.add_to_wish()
    wish_list.open_wish_list()
    wish_list.check_wish_list()
    wish_list.delete_item()
