from loguru import logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from github_task.pages.base_page import BasePage


class FindElement(BasePage):
    def find_visible_element(self, how, what):
        logger.debug(f'Trying to find visible element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            logger.error(f'Cannot find visible element "{how}", "{what}"!')
        logger.debug(f'Element "{how}", "{what}" was found...')
        return element

    def find_clickable_element(self, how, what):
        logger.debug(f'Trying to find clickable element "{how}", "{what}"...')
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            logger.error(f'Cannot find element "{how}", "{what}" or element is not clickable!')
        logger.debug(f'Clickable element "{how}", "{what}" was found...')
        return element


class ElementStatements(BasePage):
    def is_element_present(self, how, what):
        logger.info(f'Trying to find element "{how}", "{what}"...')
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logger.error(f'Cannot find element "{how}", "{what}"!')
        logger.info(f'Element "{how}", "{what}" was found...')
        return True
