import time
from loguru import logger
from .base_page import BasePage, FindElement
from .locators import *
import random
import string


class MainPage(BasePage, FindElement):

    random_name = ''.join([random.choice(string.ascii_lowercase) for i in range(10)])
    new_name = random_name + '_RENAMED'

    def is_user_correct(self, username):
        logger.warning("Is username correct started...")
        logger.info("Pressing menu button...")
        menu = self.find_clickable_element(*MainPageLocators.DROPDOWN_USERNAME_ICON_MENU)
        menu.click()
        logger.info("Is username correct check...")
        username_in_menu = self.find_visible_element(*MainPageLocators.USERNAME_IN_MENU).text
        assert username_in_menu == username, "Incorrect user is logged in"

    def create_repository(self):
        logger.warning("Creating repository started...")
        logger.info("Pressing new repository button...")
        new_button = self.find_clickable_element(*MainPageLocators.NEW_REPOSITORY_BUTTON)
        new_button.click()
        logger.info("Entering new repository name...")
        name_field = self.find_visible_element(*NewRepositoryPageLocators.REPOSITORY_NAME_FIELD)
        name_field.send_keys(self.random_name)
        logger.info("Pressing create repository button...")
        create_button = self.find_clickable_element(*NewRepositoryPageLocators.CREATE_REPOSITORY_BUTTON)
        create_button.click()

    def delete_repository(self):
        logger.warning("Deleting repository started...")
        logger.info("Pressing settings button...")
        settings_button = self.find_clickable_element(*MainPageLocators.SETTINGS_BUTTON)
        settings_button.click()
        logger.info("Pressing delete repository button...")
        delete_repository_button = self.find_clickable_element(*RepositorySettingsPageLocators.DELETE_REPOSITORY_BUTTON)
        delete_repository_button.click()
        message = self.find_visible_element(*RepositorySettingsPageLocators.PLEASE_TYPE_MESSAGE).text
        logger.info("Entering repository name in confirmation field...")
        confirmation_field = self.find_visible_element(*RepositorySettingsPageLocators.INPUT_FIELD)
        confirmation_field.send_keys(message)
        logger.info("Pressing I understand button...")
        i_understand_button = self.find_clickable_element(*RepositorySettingsPageLocators.I_UNDERSTAND_BUTTON)
        i_understand_button.click()

    def is_repository_created(self):
        logger.warning("Checking is repository created...")
        self.find_visible_element(*MainPageLocators.QUICK_SETUP_MESSAGE)
        assert self.is_element_present(*MainPageLocators.QUICK_SETUP_MESSAGE), "Repository is not created!"

    def rename_repository(self):
        logger.warning("Repository renaming started...")
        logger.info("Pressing settings button...")
        settings_button = self.find_clickable_element(*MainPageLocators.SETTINGS_BUTTON)
        settings_button.click()
        logger.info("Entering new repository name...")
        new_name_field = self.find_visible_element(*RepositorySettingsPageLocators.RENAME_REPOSITORY_FIELD)
        new_name_field.clear()
        new_name_field.send_keys(self.new_name)
        logger.info("Pressing rename button...")
        rename_button = self.find_clickable_element(*RepositorySettingsPageLocators.RENAME_BUTTON)
        rename_button.click()

    def is_repository_renamed(self):
        logger.warning("Checking is repository renamed...")
        name = self.find_visible_element(*MainPageLocators.REPOSITORY_NAME).text
        assert self.new_name == name, "Repository was not renamed!"

    def add_readme_file(self):
        logger.warning("Readme file adding started...")
        logger.info("Pressing readme adding button...")
        add_button = self.find_clickable_element(*MainPageLocators.ADD_README_BUTTON)
        add_button.click()
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
        assert self.is_element_present(*MainPageLocators.REPOSITORY_DELETED_MESSAGE), "Repository was not deleted!"
