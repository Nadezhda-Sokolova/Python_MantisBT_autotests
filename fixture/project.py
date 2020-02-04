from model.manager import Manager
import random
from model.project import Project
from data.add_project import project

class ProjectHelper(Manager):


    def open_home_page(self):
        driver = self.app.driver
        driver.get("http://localhost/mantisbt-1.2.20")

    def default_form_after_login(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("td.menu").text[-1]


    def get_manage_creation_page(self):
        driver = self.app.driver
        self.open_home_page()
        self.default_form_after_login()
        driver.find_element_by_link_text("Manage").click()
        driver.find_element_by_link_text("Manage Projects").click()


    def open_create_new_project_form(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@value='Create New Project']").click()


    def filling_info_about_project(self, project):
        driver = self.app.driver
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(project.name)
        driver.find_element_by_name("description").click()
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys(project.description)


    def add_project(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//input[@value='Add Project']").click()


    def get_id_project_for_deleting(self, project_name_to_delete):
        driver = self.app.driver
        projects_list = self.get_project_list()
        project_for_deleting = random.choice(projects_list)
        driver.find_elements_by_css_selector('table.hide td.login-info-right')
        driver.element.find_element_by_tag_name("form")
        driver.find_elements_by_css_selector('selected')



    def press_project_to_delete(self, project_name_to_delete):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[contains(text(),'%s')]" % project_name_to_delete).click()


    def delete_project(self):
        driver = self.app.driver
        driver.find_element_by_css_selector('form > input.button').click()
        #confirmation
        driver.find_element_by_xpath("//input[@value='Delete Project']").click()


    def get_project_list(self):
        driver = self.app.driver
        project_list = []
        for element in driver.find_elements_by_css_selector('table.hide td.login-info-right'):
            element.find_element_by_tag_name("form").click()
            projects = element.find_element_by_name('project_id').text
            list_of_projects = projects.split('\n')
            list_of_projects.remove('All Projects')
        return list_of_projects



#if driver.find_element_by_css_selector('form[name="form_set_project"]'):