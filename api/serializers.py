from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from .models import Profile,Employee, images

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields ='__all__'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        msg=""
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        msg="login successfull"
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'username':self.user.username})
        data.update({'user_id': self.user.id})
        data.update({'msg': msg})
        # and everything else you want to send in the response
        return data