from .locators import LoginPageLocators
from github_task.support.browser_helper import FindElement


class LoginPage(FindElement):
    def sign_in(self, username, password):
        username_input = self.find_visible_element(*LoginPageLocators.USERNAME_FIELD)
        username_input.send_keys(username)
        password_input = self.find_visible_element(*LoginPageLocators.PASSWORD_FIELD)
        password_input.send_keys(password)
        sign_in_button = self.find_clickable_element(*LoginPageLocators.SIGN_IN_BUTTON)
        sign_in_button.click()
