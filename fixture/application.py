from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper


class Application:

    def __init__(self, browser, config):
        if browser == 'firefox':
            self.driver = self.wd = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = self.wd = webdriver.IE()
        elif browser == 'chrome':
            self.driver = self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.base_url=config['web']['base_url']


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def distroy(self):
        self.wd.quit()

    # ===================

    def Open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/mantisbt-1.2.20")

    def Distroy(self):
        self.driver.quit()
