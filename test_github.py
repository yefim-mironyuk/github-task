from pages.login_page import LoginPage
from pages.main_page import MainPage
from creds import Creds
import pytest


# TYPE YOUR OWN CREDS IN "Creds.username" and "Creds.password".
username = Creds.username
password = Creds.password

link = "https://github.com/"


@pytest.fixture(scope="function")
def setup(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.sign_in(username, password)


def test_correct_user_is_logged_in(browser, setup):
    page = MainPage(browser, link)
    page.open()
    page.is_user_correct(username)


class TestRepositories():
    @pytest.fixture(scope="function", autouse=True)
    def setup_for_repositories(self, browser, setup):
        page = MainPage(browser, link)
        page.create_repository()
        yield
        page.delete_repository()

    def test_create_repository(self, browser):
        page = MainPage(browser, link)
        page.is_repository_created()

    def test_rename_repository(self, browser):
        page = MainPage(browser, link)
        page.rename_repository()
        page.is_repository_renamed()

    def test_add_readme(self, browser):
        page = MainPage(browser, link)
        page.add_readme_file()
        page.is_readme_file_added()


@pytest.fixture(scope="function")
def setup_for_deleting_repository(browser, setup):
    page = MainPage(browser, link)
    page.create_repository()


def test_delete_repository(browser, setup_for_deleting_repository):
    page = MainPage(browser, link)
    page.delete_repository()
    page.is_repository_deleted()





