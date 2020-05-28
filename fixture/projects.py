from models.project import Project

class ProjectsHelper:
    def __init__(self, app):
        self.accept_next_alert = True
        self.app = app


    def open_page_of_projects(self):
        wd = self.app.wd
        try:
            wd.find_elements_by_css_selector("#sidebar li:nth-child(7)")[0].click()
        except Exception:
            wd.find_elements_by_css_selector("#sidebar li:nth-child(6)")[0].click()
        wd.find_element_by_link_text(u"Управление проектами").click()


    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_page_of_projects()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("#main-container div:nth-child(2) div:nth-child(2) div div div:nth-child(2) div:nth-child(2) div div:nth-child(2) table tbody tr"):
                self.project_cache.append(self.resolve_project(element))
        return list(self.project_cache)


    def resolve_project(self, element):
        text_name = element.find_elements_by_css_selector('td:nth-child(1)')[0].text
        text_status = element.find_elements_by_css_selector('td:nth-child(2)')[0].text
        if text_status == 'в разработке':
            text_status = '10'
        elif text_status == 'выпущен':
            text_status = '30'
        elif text_status == 'стабильный':
            text_status = '50'
        elif text_status == 'устарел':
            text_status = '70'
        text_visibility = element.find_elements_by_css_selector('td:nth-child(4)')[0].text
        if text_visibility == 'публичный':
            text_visibility = '10'
        elif text_visibility == 'приватный':
            text_visibility = '50'
        text_description = element.find_elements_by_css_selector('td:nth-child(5)')[0].text
        return Project(name=text_name, status=text_status, visibility=text_visibility, description=text_description)


    def return_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Продолжить").click()


    def create_project(self, project):
        wd = self.app.wd
        self.open_page_of_projects()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_data(project)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()
        self.project_cache = None
        return project


    def delete_project(self, project):
        wd = self.app.wd
        self.open_page_of_projects()
        wd.find_element_by_xpath("//a[text()='%s']" % project).click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        self.project_cache = None


    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            element = wd.find_element_by_id(field_name)
            element.click()
            element.send_keys(value)


    def select_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_xpath("//select[@id='{0}']/option[@value='{1}']".format(field_name, value)).click()



    def fill_project_data(self, project):
        self.change_field_value("project-name", project.name)
        self.select_value("project-status", project.status)
        self.select_value("project-view-state", project.visibility)
        self.change_field_value("project-description", project.description)







