from .locators import *
from .main_page import MainPage


class RepositorySettingsPage(MainPage):
    def delete_repository(self):
        delete_repository_button = self.find_clickable_element(*RepositorySettingsPageLocators.DELETE_REPOSITORY_BUTTON)
        delete_repository_button.click()
        deleting_message = self.find_visible_element(*RepositorySettingsPageLocators.PLEASE_TYPE_MESSAGE).text
        confirmation_field = self.find_visible_element(*RepositorySettingsPageLocators.INPUT_FIELD)
        confirmation_field.send_keys(deleting_message)
        i_understand_button = self.find_clickable_element(*RepositorySettingsPageLocators.I_UNDERSTAND_BUTTON)
        i_understand_button.click()

    def rename_repository(self):
        new_name_field = self.find_visible_element(*RepositorySettingsPageLocators.RENAME_REPOSITORY_FIELD)
        new_name_field.clear()
        new_name_field.send_keys(self.new_name)
        rename_button = self.find_clickable_element(*RepositorySettingsPageLocators.RENAME_BUTTON)
        rename_button.click()

