from suds.client import  Client
from suds import WebFault
from models.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client('http://localhost/mantisbt-2.24.1/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def project_list(self, username, password):
        client = Client('http://localhost/mantisbt-2.24.1/api/soap/mantisconnect.php?wsdl')
        projects = []
        for i in client.service.mc_projects_get_user_accessible(username, password):
            projects.append(self.resolve_project(i))
        return list(projects)

    def resolve_project(self, i):
        name = i.name
        status = str(i.status.id)
        visibility = str(i.view_state.id)
        description = i.description
        return Project(name=name, status=status, visibility=visibility, description=description)