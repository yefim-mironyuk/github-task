from .base_page import BasePage, FindElement
from .locators import LoginPageLocators


class LoginPage(BasePage, FindElement):
    def sign_in(self, username, password):
        usernamestr = self.find_visible_element(*LoginPageLocators.USERNAME_FIELD)
        usernamestr.send_keys(username)
        passwordstr = self.find_visible_element(*LoginPageLocators.PASSWORD_FIELD)
        passwordstr.send_keys(password)
        button = self.find_clickable_element(*LoginPageLocators.SIGN_IN_BUTTON)
        button.click()
