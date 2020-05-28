import re
import quopri

class SignupHelper:
    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wd.get(self.app.baseURL+"/signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_xpath("//input[@value='Зарегистрироваться']").click()

        mail = self.app.mail.get_mail(username, password)
        url = self.extract_confirmation_url(str(mail))
        url_lenth = url[:158]
        decoded_string = quopri.decodestring(url_lenth)
        url_decoded = decoded_string.decode('utf-8').replace('=/n', '')
        wd.get(url_decoded)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_css_selector('span.bigger-110').click()


    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)





