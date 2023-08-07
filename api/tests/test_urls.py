from django.test import SimpleTestCase
from django.urls import resolve,reverse
import django
django.setup()
from api.views import *
from rest_framework_simplejwt.views import *

class TestUrls(SimpleTestCase):

    def test_signup_url_is_resolved(self):
        url=reverse("signup")
        self.assertEquals(resolve(url).func,signup)

    def test_tasklist_url_is_resolved(self):
        url=reverse("task-list",args=['1'])
        self.assertEquals(resolve(url).func,taskList)

    def test_getLeads_url_is_resolved(self):
        url=reverse("getLeads")
        self.assertEquals(resolve(url).func,getLeads)

    def test_getDetails_url_is_resolved(self):
        url=reverse("getDetails",args=['1'])
        self.assertEquals(resolve(url).func,getDetails)

    def test_getManagers_url_is_resolved(self):
        url=reverse("getManagers")
        self.assertEquals(resolve(url).func,getManagers)

    def test_getTeamTasks_url_is_resolved(self):
        url = reverse("getTeamTasks",args=['1'])
        self.assertEquals(resolve(url).func, getTeamTasks)

    def test_getRole_url_is_resolved(self):
        url = reverse("getRole",args=['1'])
        self.assertEquals(resolve(url).func, getRole)

    def test_getEmployeesUnderLead_url_is_resolved(self):
        url = reverse("getEmployeesUnderLead",args=['fname'])
        self.assertEquals(resolve(url).func, getEmployeesUnderLead)

    def test_getLeadsUnderManager_url_is_resolved(self):
        url = reverse("getLeadsUnderManager",args=['lname'])
        self.assertEquals(resolve(url).func, getLeadsUnderManager)

    def test_documents_url_is_resolved(self):
        url = reverse("documents",args=['1'])
        self.assertEquals(resolve(url).func, documents)

    def test_taskCreate_url_is_resolved(self):
        url = reverse("task-create")
        self.assertEquals(resolve(url).func, taskCreate)

    def test_deletedocument_url_is_resolved(self):
        url = reverse("delete-document",args=['1'])
        self.assertEquals(resolve(url).func, deletedocument)

    def test_imageSave_url_is_resolved(self):
        url = reverse("imageSave")
        self.assertEquals(resolve(url).func, imageSave)

    def test_taskUpdate_url_is_resolved(self):
        url = reverse("task-update",args=['1'])
        self.assertEquals(resolve(url).func, taskUpdate)

    def test_taskDelete_url_is_resolved(self):
        url = reverse("task-delete",args=['1'])
        self.assertEquals(resolve(url).func, taskDelete)

    def test_token_refresh_url_is_resolved(self):
        url = reverse("token_refresh")
        self.assertEquals(resolve(url).func.view_class, TokenRefreshView)

    def test_token_obtain_pair_url_is_resolved(self):
        url = reverse("token_obtain_pair")
        self.assertEquals(resolve(url).func.view_class, MyTokenObtainPairView)



