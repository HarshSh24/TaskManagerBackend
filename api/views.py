from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import TaskSerializer,ProfileSerializer, UserSerializer, EmployeeSerializer,ImageSerializer
from rest_framework.permissions import AllowAny
from .models import Task, Profile, Employee, images
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from allauth.account.signals import user_logged_in
# Create your views here.


# @csrf_exempt
# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def profile_view(request, format=None):
#     content = {
#         'user': str(request.user),  # `django.contrib.auth.User` instance.
#         'auth': str(request.auth),  # None
#     }
#     return Response(content)

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny, ])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def taskList(request,pk):

	tasks = Task.objects.filter(parent=pk)
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def getDetails(request,pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks)
	return Response(serializer.data)

@api_view(['GET'])
def getRole(request,pk):
	role=Profile.objects.get(username_id=pk)
	serializer = ProfileSerializer(role)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny, ])
def getLeads(request):
	names=[]
	leads=Profile.objects.filter(role="teamlead")
	serializer = ProfileSerializer(leads,many=True)
	# for x in serializer.data:
	# 	names.append(User.objects.get(id=(x.data)["username_id"]))
	for x in serializer.data:
		names.append(User.objects.get(id=x["username_id"]))
	serializer = UserSerializer(names, many=True)
	leads=[]
	for x in serializer.data:
		leads.append(x["username"])
	return Response(leads)
@api_view(['GET'])
@permission_classes([AllowAny, ])
def getManagers(request):
	names=[]
	managers=Profile.objects.filter(role="manager")
	serializer = ProfileSerializer(managers,many=True)
	# for x in serializer.data:
	# 	names.append(User.objects.get(id=(x.data)["username_id"]))
	for x in serializer.data:
		names.append(User.objects.get(id=x["username_id"]))
	serializer = UserSerializer(names, many=True)
	managers=[]
	for x in serializer.data:
		managers.append(x["username"])
	return Response(managers)

@api_view(['GET'])
def getTeamTasks(request,pk):
	lead=Employee.objects.get(username_id=pk)
	serializer = EmployeeSerializer(lead)
	lead=serializer.data['lead']
	tasks=Task.objects.filter(username=lead)
	serializer=TaskSerializer(tasks,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def documents(request,pk):
	try:
		documents = images.objects.filter(user_id=pk)
		links = []
		serializer = ImageSerializer(documents,many=True)
		for x in serializer.data:
			links.append([x["id"],x["link"]])
	except:
		return({})
	return Response(serializer.data)

@api_view(['GET'])
def getEmployeesUnderLead(request,lname):
	employees_list=[]
	employees=Employee.objects.filter(lead=lname)
	serializer = EmployeeSerializer(employees, many=True)
	for x in serializer.data:
		employees_list.append(User.objects.get(id=x["username_id"]))
	serializer=UserSerializer(employees_list,many=True)
	names=[]
	for x in serializer.data:
		names.append(x["username"])
	return Response(names)

@api_view(['GET'])
def getLeadsUnderManager(request,mname):
	leads_list=[]
	leads=Employee.objects.filter(lead=mname)
	serializer = EmployeeSerializer(leads, many=True)
	for x in serializer.data:
		leads_list.append(User.objects.get(id=x["username_id"]))
	serializer=UserSerializer(leads_list,many=True)
	names=[]
	for x in serializer.data:
		names.append(x["username"])
	return Response(names)





@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data.get('id'))
	else:
		return Response("object not found", status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def imageSave(request):
	serializer = ImageSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response("Task successfully updated")
	else:
		return Response("object not found", status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Task successfully deleted!')

@api_view(['DELETE'])
def deletedocument(request, pk):
	doc = images.objects.get(id=pk)
	doc.delete()

	return Response('document successfully deleted!')





# class CustomAuthToken(ObtainAuthToken):
#
# 	def post(self, request, *args, **kwargs):
# 		serializer = self.serializer_class(data=request.data,
# 											context={'request': request})
# 		try:
# 			serializer.is_valid(raise_exception=True)
# 			user = serializer.validated_data['user']
# 			token, created = Token.objects.get_or_create(user=user)
# 			return Response({
# 				'token': token.key,
# 				'username':user.username,
# 				'user_id': user.pk,
# 				'email': user.email,
# 				'msg':"login successfull"
# 			})
# 		except:
# 			return Response({'msg':"invalid credentials"})


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	permission_classes=(AllowAny),
	def validate(self, attrs):
		msg=""
		data = super().validate(attrs)
		# refresh = self.get_token(self.user)
		# print("****",refresh)
		msg="login successfull"
		data['username']=self.user.username
		data['id']=self.user.id
		data['user_id'] = self.user.id
		data['msg'] = msg
		data['groups'] = self.user.groups.values_list('name', flat=True)
		print(data)
		return data

class MyTokenObtainPairView(TokenObtainPairView):
	permission_classes = (AllowAny),
	serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
	try:
		username = request.data['username']
		password = request.data['password']
		user = User.objects.get(username=username)
		msg=""
		if user:
			try:
				payload = jwt_payload_handler(user)
				token = jwt_encode_handler(payload)
				print(token)
				user_details = {}
				user_details['user_id']=user.pk
				user_details['username']=username
				user_details['token'] = token
				user_logged_in.send(sender=user.__class__,
									request=request, user=user)
				user_details['msg']="login successfull"
				return Response(user_details, status=status.HTTP_200_OK)
			except Exception as e:
				raise e
		else:
			res = {
					'error': 'can not authenticate with the given credentials or the account has been deactivated'}
			return Response(res, status=status.HTTP_403_FORBIDDEN)
	except KeyError:
		res = {'error': 'please provide a email and a password'}
		return Response(res)

@api_view(['POST'])
@permission_classes([AllowAny, ])
def signup(request):
	username = request.data.get('username')
	password = request.data.get('password')
	role = request.data.get('role')
	lead = request.data.get('lead')
	manager = request.data.get('manager')
	try:
		if(username!=""):
			user = User.objects.create_user(username,"",password)
		else:
			return Response("username cannot be empty", status.HTTP_400_BAD_REQUEST)
		serializer = ProfileSerializer(data={"username_id":user.pk,"role":role})
		if serializer.is_valid():
			serializer.save()
		if lead!="":
			serializer = EmployeeSerializer(data={"username_id":user.pk,"lead":lead})
			if serializer.is_valid():
				serializer.save()
		if manager!="":
			serializer = EmployeeSerializer(data={"username_id":user.pk,"lead":manager})
			if serializer.is_valid():
				serializer.save()
		token = Token.objects.create(user=user)
		return Response("user registered successfully")
	except Exception:
		return Response("this username already exists")



