from tests.page_object.BasePage import BasePage


class SingUp(BasePage):
    def open_register(self):
        acc = self.find_of_element_class_name("caret")
        self.click(acc)
        link = self.find_of_element_link("Register")
        self.click(link)

    def input_firstname(self):
        first_name = "Milena"
        self.input("firstname", first_name)

    def input_lastname(self):
        last_name = "Chudakova"
        self.input("lastname", last_name)

    def input_email(self):
        e_mail = "chudakovamilena587@gmail.com"
        self.input("email", e_mail)

    def input_telephone(self):
        number = "25255255255"
        self.input("telephone", number)

    def input_password(self):
        password = "12345678qwe"
        self.input("password", password)

    def input_confirm_password(self):
        password = "12345678qwe"
        self.input("confirm", password)

    def button_continue(self):
        continue_button = self.find_of_element_path("//input[@type='submit'][@value='Continue']")
        self.click(continue_button)
