from model.manager import Manager
from suds.client import Client
from suds import WebFault
import json


class SoapHelper(Manager):


    def can_login(self, username, password):
        client = Client('http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_num_projects(self, username, password):

        client = Client(self.app.config['web']['base_url']+'/api/soap/mantisconnect.php?wsdl')
        try:
            response = client.service.mc_projects_get_user_accessible(username, password)
            L = []
            for project_data in response:
                project = project_data.name
                L.append(str(project))
            return L
        except WebFault as e:
            print|(e)





            response = client.service.mc_projects_get_user_accessible(username, password)
            L = []
            # parsed_response = json.loads(response)
            print(response)

            for project in response:
                project = {"id": project.id, "name": project.name, 'status':project.status, 'enabled':project.enabled,
                           'view_state':project.view_state, 'access_min':project.access_min, 'description':project.description}
                L.append(project)
            return json.dumps({"results":L})

            # (id, name, status, inherit_global, enabled, view_state, access_min, file_path, description) = project
                # parsed_response = json.load(Project(id=id, name=name, status=status, inherit_global=inherit_global, view_state=view_state,
                #         description=description), 'r')
                # print(parsed_response)
            #     L.append()


        except WebFault as e:
            print(e)



