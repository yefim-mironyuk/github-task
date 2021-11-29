from loguru import logger
from .locators import *
from .main_page import MainPage


class NewRepositoryPage(MainPage):

    def create_repository(self):
        logger.info("Entering new repository name...")
        name_field = self.find_visible_element(*NewRepositoryPageLocators.REPOSITORY_NAME_FIELD)
        name_field.send_keys(self.random_name)
        logger.info("Pressing create repository button...")
        create_button = self.find_clickable_element(*NewRepositoryPageLocators.CREATE_REPOSITORY_BUTTON)
        create_button.click()
