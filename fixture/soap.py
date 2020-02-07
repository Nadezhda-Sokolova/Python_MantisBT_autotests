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
            response = client.service.mc_enum_projections(username, password)
            return list(response)
        except WebFault:
            return False

