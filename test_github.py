from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.new_repository_page import NewRepositoryPage
from .pages.repository_settings_page import RepositorySettingsPage
import pytest
from .support.creds import Creds


link = "https://github.com/login"


@pytest.fixture(scope="function")
def setup(browser):
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.sign_in(Creds.username, Creds.password)


def test_correct_user_is_logged_in(browser, setup):
    main_page = MainPage(browser, link)
    main_page.is_user_correct(Creds.username)


class TestRepositories():
    @pytest.fixture(scope="function", autouse=True)
    def setup_for_repositories(self, browser, setup):
        main_page = MainPage(browser, link)
        main_page.go_to_new_repository_page()
        new_repository_page = NewRepositoryPage(browser, link)
        new_repository_page.create_repository()
        yield
        main_page.go_to_settings_page()
        settings_page = RepositorySettingsPage(browser, link)
        settings_page.delete_repository()

    def test_create_repository(self, browser):
        main_page = MainPage(browser, link)
        main_page.is_repository_created()

    def test_rename_repository(self, browser):
        main_page = MainPage(browser, link)
        main_page.go_to_settings_page()
        settings_page = RepositorySettingsPage(browser, link)
        settings_page.rename_repository()
        main_page.is_repository_renamed()

    def test_add_readme(self, browser):
        main_page = MainPage(browser, link)
        main_page.add_readme_file()
        main_page.is_readme_file_added()


@pytest.fixture(scope="function")
def setup_for_deleting_repository(browser, setup):
    main_page = MainPage(browser, link)
    main_page.go_to_new_repository_page()
    new_repository_page = NewRepositoryPage(browser, link)
    new_repository_page.create_repository()

def test_delete_repository(browser, setup_for_deleting_repository):
    main_page = MainPage(browser, link)
    main_page.go_to_settings_page()
    settings_page = RepositorySettingsPage(browser, link)
    settings_page.delete_repository()
    main_page.is_repository_deleted()





