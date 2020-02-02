import random

def test_to_delete_project_to_Mantis(app, check_ui):
    app.session.login("administrator", "root")
    app.project.get_manage_creation_page()
    old_project_list = app.project.get_project_list()
    project_name_to_delete = random.choice(old_project_list)
    app.project.press_project_to_delete(project_name_to_delete)
    app.project.delete_project()
    app.project.get_manage_creation_page()
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    if check_ui:
        assert sorted(old_project_list) == sorted(new_project_list)
    app.session.logout()



