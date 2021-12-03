from github_task.support.logging import Logger


class BasePage(Logger):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
