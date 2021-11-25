from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def sign_in(self, username, password, browser):
        usernamestr = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.USERNAME_FIELD)))
        usernamestr.send_keys(username)
        passwordstr = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        passwordstr.send_keys(password)
        button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((LoginPageLocators.SIGN_IN_BUTTON)))
        button.click()
