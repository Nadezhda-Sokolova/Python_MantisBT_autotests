from model.manager import Manager
from suds.client import Client
from suds import WebFault

class SoapHelper(Manager):


    def can_login(self, username, password):
        client = Client('http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_num_projects(self, username, password):
        client = Client('http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl')
        try:
            response = client.service.mc_projects_get_user_accessible(username, password)
            return (response)
        except WebFault as e:
            return e

