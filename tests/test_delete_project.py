from models.project import Project
from random import randrange

def test_add_project(app):
    username = 'administrator'
    password = 'root'
    app.session.login(username, password)
    if len(app.soap.project_list(username, password)) == 0:
        app.projects.create_project(Project(name="test"))
    old_projects = app.soap.project_list(username, password)
    index = randrange(len(old_projects))
    element_to_delete = sorted(old_projects, key=Project.name)[index]
    old_name = element_to_delete.name
    app.projects.delete_project(old_name)
    new_projects = app.soap.project_list(username, password)
    element_actually_deleted = list(set(old_projects) - set(new_projects))[0]
    assert element_actually_deleted == element_to_delete