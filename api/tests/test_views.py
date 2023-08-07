# from django.test import TestCase,Client
# from django.urls import reverse
# import django
# django.setup()
# from api.models import *
# import json
# import requests
# from rest_framework.test import APIClient
# from rest_framework.test import force_authenticate
# from api.views import MyTokenObtainPairView
#
# class TestViews(TestCase):
#
#     def setUp(self):
#         self.client=APIClient()
#         lead1=User.objects.create(username="testlead",password="test@password")
#         manager1= User.objects.create(username="testmanager",email="",password="test@password",is_active=True)
#         self.c=Task.objects.create(title="testing",status="completed",username="testlead",assignedto="testemp",parent=0)
#         p1=Profile.objects.create(username_id=lead1,role="teamlead")
#         p2 = Profile.objects.create(username_id=manager1, role="manager")
#         e= Employee.objects.create(username_id=lead1,lead="lead1")
#         im= images.objects.create(user_id=3,link="dummy.com")
#         self.taskList_url = reverse('task-list',args=['0'])
#         self.getRole_url = reverse('getRole',args=[lead1.id])
#         self.getDetails_url = reverse('getDetails',args=[self.c.id])
#         self.getLeads_url=reverse('getLeads')
#         self.getManagers_url = reverse('getManagers')
#         self.getTeamTasks_url = reverse('getTeamTasks',args=[e.username_id.id])
#         self.documents_url = reverse('documents',args=[e.id])
#         self.getEmployeesUnderLead_url = reverse('getEmployeesUnderLead',args=[lead1.username])
#         self.getLeadsUnderManager_url = reverse('getLeadsUnderManager',args=[manager1.username])
#         self.taskCreate_url = reverse('task-create')
#         self.taskUpdate_url= reverse('task-update',args=[self.c.id])
#         self.taskDelete_url=reverse('task-delete',args=[self.c.id])
#         self.documentDelete_url = reverse('delete-document', args=[im.id])
#         self.imagesave_url= reverse('imageSave')
#         self.signup_url= reverse('signup')
#         x=requests.post("http://127.0.0.1:8000/signup/",json={"username": "testmanager","password": "test@password"})
#         x = requests.post("http://127.0.0.1:8000/accounts/api/auth/", json={"username": "testmanager","password": "test@password"})
#         self.token = (x.json()["access"])
#
#
#     def test_task_list(self):
#         header = {'Authorization': 'Bearer ' + self.token}
#         response= self.client.get(self.taskList_url,header=header)
#         print(response)
#         #self.assertEquals(response.status_code,200)
#
#     # def test_getRole(self):
#     #     response= self.client.get(self.getRole_url,header=self.header)
#     #     self.assertEquals(response.status_code,200)
#     #
#     # def test_getDetails(self):
#     #     response = self.client.get(self.getDetails_url,header=self.header)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_getLead(self):
#     #     response = self.client.get(self.getLeads_url)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_getManager(self):
#     #     response = self.client.get(self.getManagers_url)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_getTeamTasks(self):
#     #     response = self.client.get(self.getTeamTasks_url,header=self.header)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_documents(self):
#     #     response= self.client.get(self.documents_url,header=self.header)
#     #     self.assertEquals(response.status_code,200)
#     #
#     # def test_getEmployeesUnderLead_url(self):
#     #     response = self.client.get(self.getEmployeesUnderLead_url,header=self.header)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_getLeadsUnderManager(self):
#     #     response = self.client.get(self.getLeadsUnderManager_url,header=self.header)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_taskCrete(self):
#     #     response = self.client.post(self.taskCreate_url,{
#     #         "title":"testing_task", 'status' : "pending",'username': "testlead", 'assignedto': "testemp",'parent': 1
#     #     },header=self.header)
#     #     self.assertEquals(response.status_code,200)
#     #
#     # def test_taskCrete_missing_data(self):
#     #     response = self.client.post(self.taskCreate_url,{
#     #         "title":"","status" : "pending","username": "testlead", "assignedto": "testemp","parent": 1
#     #     },header=self.header)
#     #     self.assertEquals(response.status_code,400)
#     #
#     # def test_task_update(self):
#     #     response = self.client.put(self.taskUpdate_url, content_type='application/json',data=json.dumps({
#     #         "title": "testing_task", "status": "inprogress", "username": "testlead", "assignedto": "testemp", "parent": 1,
#     #     }),header=self.header)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_task_update_missing_id(self):
#     #     x = requests.post("http://127.0.0.1:8000/accounts/api/auth/", json={"username": "lead1", "password": "12"})
#     #     dummy_token = (x.json()["access"])
#     #     header = {'Authorization': 'Bearer ' + dummy_token}
#     #     response = self.client.put(self.taskUpdate_url,content_type='application/json',data= json.dumps({
#     #         "title": "", "status": "inprogess", "username": "testlead", "assignedto": "testemp", "parent": 1
#     #     }),header=self.header)
#     #     self.assertEquals(response.status_code, 400)
#     #
#     # def test_task_delete_url(self):
#     #     x = requests.post("http://127.0.0.1:8000/accounts/api/auth/", json={"username": "lead1", "password": "12"})
#     #     dummy_token = (x.json()["access"])
#     #     header = {'Authorization': 'Bearer ' + dummy_token}
#     #     response= self.client.delete(self.taskDelete_url,header=self.header)
#     #     self.assertEquals(response.status_code,200)
#     #
#     # def test_document_delete_url(self):
#     #     response= self.client.delete(self.documentDelete_url,header=self.header)
#     #     self.assertEquals(response.status_code,200)
#     #
#     # def test_imagesave_url(self):
#     #     response= self.client.post(self.imagesave_url,{"user_id":2,"link":"dummylink.com"},header=self.header)
#     #     self.assertEquals(response.status_code, 200)
#     #
#     # def test_signup_url(self):
#     #     response= self.client.post(self.signup_url,{"username":"user43","email":"","password":"fake@123#"})
#     #     self.assertEquals(response.status_code,200)
#     #
#     # def test_signup_url_invalid_password(self):
#     #     response= self.client.post(self.signup_url,{"username":"","password":"12"})
#     #     self.assertEquals(response.status_code,400)
#
#
#
#
#
#
#
#
