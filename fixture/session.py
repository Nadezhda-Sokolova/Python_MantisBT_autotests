from model.manager import Manager

class SessionHelper (Manager):


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[contains(@href, ''/mantisbt-1.2.20/logout_page.php'')]').click()
        self.app.open_home_page()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

#======

    def Login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)

    def ensure_Logout(self):
        driver = self.app.driver
        if self.is_Logged_in():
            self.Logout()

    def is_Logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_Logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div[@id='top']/form/b").text == "("+username+")"

    def Logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_Login(self, username, password):
        driver = self.app.driver
        if self.is_Logged_in():
            if self.is_Logged_in_as(username):
                return
            else:
                self.Logout()
        self.Login(username, password)
