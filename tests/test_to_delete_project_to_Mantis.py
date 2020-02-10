import random
from model.project import Project
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range (random.randrange(maxlen))])


def test_to_delete_project_to_Mantis(app, check_ui):
    app.session.login("administrator", "root")
    app.project.get_manage_creation_page()
    i=0
    a = [random_string('name', 10), random_string('name', 10), random_string('name', 10)]
    while i  < 3:
        app.project.open_create_new_project_form()
        app.project.filling_info_about_project(Project(name=a[i], status='development',
           inherit_global="checked", description='add one more'))
        app.project.add_project()
        app.project.get_manage_creation_page()
        i+=1

    old_SOAP_list = app.soap.get_num_projects("administrator", "root")

    app.project.get_manage_creation_page()
    old_project_list = app.project.get_project_list()
    project_name_to_delete = random.choice(old_project_list)
    app.project.press_project_to_delete(project_name_to_delete)
    app.project.delete_project()

    new_SOAP_list = app.soap.get_num_projects("administrator", "root")
    assert len(old_SOAP_list) - 1 == len(new_SOAP_list)

    app.project.get_manage_creation_page()
    new_project_list = app.project.get_project_list()

    new_project_list.append(project_name_to_delete)
    assert sorted(old_project_list) == sorted(new_project_list)
    app.session.logout()



