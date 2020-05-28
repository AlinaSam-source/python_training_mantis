from selenium import webdriver
from fixture.session import SessionHelper
from fixture.projects import ProjectsHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
from generator import project


class Application:
    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.projects = ProjectsHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.baseURL = config['web']['baseURL']
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.project = project


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseURL)

    def destroy(self):
        self.wd.quit()
