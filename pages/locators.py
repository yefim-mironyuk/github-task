from selenium.webdriver.common.by import By
import time


class MainPageLocators():
    DROPDOWN_USERNAME_ICON_MENU = (
        By.CSS_SELECTOR,
        "div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > span.dropdown-caret"
    )
    USERNAME_IN_MENU = (
        By.CSS_SELECTOR,
        "div.header-nav-current-user.css-truncate > a > strong"
    )
    NEW_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "#repos-container > h2 > a")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "#settings-tab > span:nth-child(2)")
    QUICK_SETUP_MESSAGE = (By.CSS_SELECTOR, "div.Box-header")
    REPOSITORY_NAME = (By.CSS_SELECTOR, "h1 > strong > a")
    ADD_README_BUTTON = (By.CSS_SELECTOR, "p > a:nth-child(3)")
    README_TEXT_FIELD = (By.CSS_SELECTOR, "#code-editor > div > pre")
    SUBMIT_NEW_README_FILE = (By.CSS_SELECTOR, "#submit-file")
    README_WINDOW = (By.CSS_SELECTOR, "#readme")
    REPOSITORY_DELETED_MESSAGE = (By.CSS_SELECTOR, "#js-flash-container > div")


class LoginPageLocators():
    USERNAME_FIELD = (By.CSS_SELECTOR, "#login_field")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-block.js-sign-in-button")


class BasePageLocators():
    SIGN_IN_HEADER = (By.CSS_SELECTOR, ".HeaderMenu-link.flex-shrink-0.no-underline")


class NewRepositoryPageLocators():
    REPOSITORY_NAME_FIELD = (By.CSS_SELECTOR, "#repository_name")
    CREATE_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "div.js-with-permission-fields > button")


class RepositorySettingsPageLocators():
    DELETE_REPOSITORY_BUTTON = (By.CSS_SELECTOR, "li:nth-child(4) > details > summary")
    PLEASE_TYPE_MESSAGE = (
        By.CSS_SELECTOR,
        "div.Box-body.overflow-auto > p:nth-child(1) > strong:nth-child(2)"
    )
    INPUT_FIELD = (By.CSS_SELECTOR, "div.Box-body.overflow-auto > form > p > input")
    I_UNDERSTAND_BUTTON = (By.CSS_SELECTOR, "div.Box-body.overflow-auto > form > button")
    RENAME_REPOSITORY_FIELD = (By.CSS_SELECTOR, "#rename-field")
    RENAME_BUTTON = (By.CSS_SELECTOR, "form.d-flex > button")
