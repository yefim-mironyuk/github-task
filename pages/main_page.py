from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import *
import random
import string


class MainPage(BasePage):
    random_name = ''.join([random.choice(string.ascii_lowercase) for i in range(10)])
    new_name = random_name + '_RENAMED'

    def is_user_correct(self, username):
        menu = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.DROPDOWN_USERNAME_ICON_MENU)))
        menu.click()
        username_in_menu = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((MainPageLocators.USERNAME_IN_MENU))).text
        assert username_in_menu == username, "Incorrect user is logged in"

    def create_repository(self):
        new_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.NEW_REPOSITORY_BUTTON)))
        new_button.click()
        name_field = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((NewRepositoryPageLocators.REPOSITORY_NAME_FIELD)))
        name_field.send_keys(self.random_name)
        create_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((NewRepositoryPageLocators.CREATE_REPOSITORY_BUTTON)))
        create_button.click()

    def delete_repository(self):
        settings_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.SETTINGS_BUTTON)))
        settings_button.click()
        delete_repository_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((RepositorySettingsPageLocators.DELETE_REPOSITORY_BUTTON)))
        delete_repository_button.click()
        message = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((RepositorySettingsPageLocators.PLEASE_TYPE_MESSAGE))).text
        confirmation_field = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((RepositorySettingsPageLocators.INPUT_FIELD)))
        confirmation_field.send_keys(message)
        i_understand_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((RepositorySettingsPageLocators.I_UNDERSTAND_BUTTON)))
        i_understand_button.click()

    def is_repository_created(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((MainPageLocators.QUICK_SETUP_MESSAGE)))
        assert self.is_element_present(*MainPageLocators.QUICK_SETUP_MESSAGE), "Repository is not created!"

    def rename_repository(self):

        settings_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.SETTINGS_BUTTON)))
        settings_button.click()
        new_name_field = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((RepositorySettingsPageLocators.RENAME_REPOSITORY_FIELD)))
        new_name_field.clear()
        new_name_field.send_keys(self.new_name)
        rename_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((RepositorySettingsPageLocators.RENAME_BUTTON)))
        rename_button.click()

    def is_repository_renamed(self):
        name = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((MainPageLocators.REPOSITORY_NAME))).text
        assert self.new_name == name, "Repository was not renamed!"

    def add_readme_file(self):
        add_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.ADD_README_BUTTON)))
        add_button.click()
        text_field = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((MainPageLocators.README_TEXT_FIELD)))
        text_field.click()
        text_field.send_keys("\n THIS FILE WAS CREATED BY COMPUTER")
        time.sleep(5)
        submit_button = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.SUBMIT_NEW_README_FILE)))
        submit_button.click()

    def is_readme_file_added(self):
        assert self.is_element_present(*MainPageLocators.README_WINDOW), "ReadMe file was not created!"

    def is_repository_deleted(self):
        assert self.is_element_present(*MainPageLocators.REPOSITORY_DELETED_MESSAGE), "Repository was not deleted!"
