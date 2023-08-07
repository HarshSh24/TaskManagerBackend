from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
	#path('accounts/profile/', csrf_exempt(views.profile_view), name="api-overview"),
	path('', views.apiOverview, name="api-overview"),
	path('signup/', views.signup, name="signup"),
	path('task-list/<str:pk>/', views.taskList, name="task-list"),
	path('getLeads/', views.getLeads, name="getLeads"),
	path('getDetails/<str:pk>', views.getDetails, name="getDetails"),
	path('getManagers/', views.getManagers, name="getManagers"),
	path('getTeamTasks/<str:pk>',views.getTeamTasks,name="getTeamTasks"),
	path('getRole/<str:pk>/', views.getRole, name="getRole"),
	path('getEmployeesUnderLead/<str:lname>/', views.getEmployeesUnderLead, name="getEmployeesUnderLead"),
	path('getLeadsUnderManager/<str:mname>/', views.getLeadsUnderManager, name="getLeadsUnderManager"),
	path('documents/<str:pk>/', views.documents, name="documents"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('delete-document/<str:pk>/', views.deletedocument, name="delete-document"),
	path('imageSave/', views.imageSave, name="imageSave"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
	path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
	path('accounts/api/auth/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
