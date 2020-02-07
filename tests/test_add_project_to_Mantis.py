from model.project import Project
import pytest
from data.add_project import project

@pytest.mark.parametrize('project', project, ids=[repr(x) for x in project])
def test_add_project_to_Mantis(app, project, check_ui):
    old_SOAP_list = app.soap.get_num_projects("administrator", "root")
    print(old_SOAP_list)

    app.session.login("administrator", "root")
    app.project.get_manage_creation_page()
    old_project_list = app.project.get_project_list()
    app.project.open_create_new_project_form()
    app.project.filling_info_about_project(project)
    app.project.add_project()
    app.project.get_manage_creation_page()
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)

    #verificartion from API via SOAP
    new_SOAP_list = app.soap.get_num_projects("administrator", "root")
    print(new_SOAP_list)

    assert new_SOAP_list-old_SOAP_list == 1

    # varification from UI
    # assert len(old_project_list)+1 == len(new_project_list)
    #     # if check_ui:
    #     #     assert sorted(old_project_list) == sorted(new_project_list)
    #     # app.session.logout()
    #     # app.open_home_page()





