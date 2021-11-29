import time
from loguru import logger
from .locators import *
from github_task.support.browser_helper import FindElement, ElementStatements
import random
import string


class MainPage(FindElement, ElementStatements):
    random_name = ''.join([random.choice(string.ascii_lowercase) for i in range(10)])
    new_name = random_name + '_RENAMED'

    def is_user_correct(self, username):
        logger.info("Pressing menu button...")
        menu = self.find_clickable_element(*MainPageLocators.DROPDOWN_USERNAME_ICON_MENU)
        menu.click()
        username_in_menu = self.find_visible_element(*MainPageLocators.USERNAME_IN_MENU).text
        assert username_in_menu == username, "Incorrect user is logged in"

    def go_to_new_repository_page(self):
        logger.info("Pressing new repository button...")
        new_repository_button = self.find_clickable_element(*MainPageLocators.NEW_REPOSITORY_BUTTON)
        new_repository_button.click()

    def go_to_settings_page(self):
        logger.info("Pressing settings button...")
        settings_button = self.find_clickable_element(*MainPageLocators.SETTINGS_BUTTON)
        settings_button.click()

    def is_repository_created(self):
        self.find_visible_element(*MainPageLocators.QUICK_SETUP_MESSAGE)
        assert self.is_element_present(*MainPageLocators.QUICK_SETUP_MESSAGE), "Repository is not created!"

    def is_repository_renamed(self):
        name = self.find_visible_element(*MainPageLocators.REPOSITORY_NAME).text
        assert self.new_name == name, "Repository was not renamed!"

    def add_readme_file(self):
        logger.info("Pressing readme adding button...")
        add_readme_button = self.find_clickable_element(*MainPageLocators.ADD_README_BUTTON)
        add_readme_button.click()
        logger.info("Entering content in text field...")
        text_field = self.find_visible_element(*MainPageLocators.README_TEXT_FIELD)
        text_field.click()
        text_field.send_keys("\n THIS FILE WAS CREATED BY COMPUTER")
        time.sleep(3)
        logger.info("Pressing submit button...")
        submit_button = self.find_clickable_element(*MainPageLocators.SUBMIT_NEW_README_FILE)
        submit_button.click()

    def is_readme_file_added(self):
        logger.warning("Checking is readme file created...")
        assert self.is_element_present(*MainPageLocators.README_WINDOW), "ReadMe file was not created!"

    def is_repository_deleted(self):
        logger.warning("Checking is repository deleted...")
        assert self.random_name not in self.find_visible_element(
            *MainPageLocators.REPOSITORIES).text, "Repository was not deleted!"
