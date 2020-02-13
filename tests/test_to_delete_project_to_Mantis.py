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

    # verification from SOAP

    new_SOAP_list = app.soap.get_num_projects("administrator", "root")
    assert len(old_SOAP_list) - 1 == len(new_SOAP_list)
    project_for_d = [j for j in old_SOAP_list if j.name == project_name_to_delete]
    print(old_SOAP_list)
    print(project_for_d)
    new_SOAP_list.append(project_for_d)
    if check_ui:
        assert sorted(old_SOAP_list) == sorted(new_SOAP_list)


   # verification from UI

    # app.project.get_manage_creation_page()
    # new_project_list = app.project.get_project_list()
    # new_project_list.append(project_name_to_delete)
    # assert sorted(old_project_list) == sorted(new_project_list)
    # app.session.logout()


    # verification from full SOAP data of response

    # i=0
    # L=[]
    # while i < (len(old_SOAP_list)-1):
    #     L.append(old_SOAP_list[i][1])
    #     i=i+1
    # print (L)
    #
    # j = 0
    # L1 = []
    # while j < (len(old_SOAP_list) - 1):
    #     L1.append(old_SOAP_list[j]['name'])
    #     j = j + 1
    # print(L)
    #
    # L.remove(project_name_to_delete)
    #
    # if check_ui:
    #     assert sorted(L) == sorted(L1)
    # app.session.logout()
    # app.open_home_page()








