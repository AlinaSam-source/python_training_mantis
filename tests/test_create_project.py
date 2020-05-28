from models.project import Project

def test_add_project(app, json_projects):
    app.project
    username = 'administrator'
    password = 'root'
    app.session.login(username, password)
    old_projects = app.soap.project_list(username, password)
    project = json_projects
    app.projects.create_project(project)
    new_projects = app.soap.project_list(username, password)
    old_projects.append(project)
    app.session.logout()
    assert sorted(new_projects, key=Project.name) == sorted(old_projects, key=Project.name)



