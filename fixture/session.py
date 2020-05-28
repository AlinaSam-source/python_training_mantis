class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_xpath("//input[@value='Войти']").click()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Войти']").click()


    def logout(self):
        wd = self.app.wd
        # wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[2]/a/i[2]").click()
        wd.find_element_by_css_selector('.ace-icon:nth-child(3)').click()
        wd.find_element_by_link_text("Выход").click()


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0


    def is_logged_in_as(self, username):
        return self.get_logged_user() == username


    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text


    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
