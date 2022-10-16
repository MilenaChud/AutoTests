from tests.page_object.BasePage import BasePage


class WishList(BasePage):

    def open_catalog(self):
        components = self.find_of_element_link("Components")
        self.click(components)
        monitors = self.find_of_element_link("Monitors (2)")
        self.click(monitors)

    def add_to_wish(self):
        wish = self.find_of_element_css("[data-original-title='Add to Wish List']")
        self.click(wish)

    def open_wish_list(self):
        check = self.find_of_element_id("wishlist-total")
        self.click(check)

    def check_wish_list(self):
        e_mail = "chudakovamilena587@gmail.com"
        password = "12345678qwe"
        self.input("email", e_mail)
        self.input("password", password)
        continue_button = self.find_of_element_path("//input[@type='submit'][@value='Login']")
        self.click(continue_button)
        table = self.find_of_element_class_name("table table-bordered table-hover")

    def delete_item(self):
        wish = self.find_of_element_css("[data-original-title='Remove']")
        self.click(wish)


