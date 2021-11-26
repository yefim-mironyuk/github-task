from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators

logger.remove()
logger.add("debug.log", format="{time:DD:MM:YYYY:h:m:s} {level} {message}", level="DEBUG")


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        logger.info(f'Trying to find element "{how}", "{what}"...')
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logger.error(f'Cannot find element "{how}", "{what}"!')
            return False
        logger.info(f'Element "{how}", "{what}" was found...')
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        logger.warning("Going to login page...")
        button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((BasePageLocators.SIGN_IN_HEADER)))
        button.click()


class FindElement():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find_visible_element(self, how, what):
        logger.debug(f'Trying to find element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            logger.error(f'Cannot find element "{how}", "{what}"!')
            return False
        logger.debug(f'Element "{how}", "{what}" was found...')
        return element

    def find_clickable_element(self, how, what):
        logger.debug(f'Trying to find element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            logger.error(f'Cannot find element "{how}", "{what}" or element is not clickable!')
            return False
        logger.debug(f'Element "{how}", "{what}" was found...')
        return element



