from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest
import allure

username = "TA-user"
password = "TAInternship11"

link = "https://github.com/"


@pytest.fixture(scope="function")
def setup(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.sign_in(username, password, browser)


class TestCorrectUser():
    @pytest.mark.dick2
    def test_correct_user_is_logged_in(self, browser, setup):
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

    @pytest.mark.dick2
    def test_create_repository(self, browser):
        page = MainPage(browser, link)
        page.is_repository_created()

    @pytest.mark.dick2
    def test_rename_repository(self, browser):
        page = MainPage(browser, link)
        page.rename_repository()
        page.is_repository_renamed()

    @pytest.mark.dick3
    def test_add_readme(self, browser):
        page = MainPage(browser, link)
        page.add_readme_file()
        page.is_readme_file_added()




