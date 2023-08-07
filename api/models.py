from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
# Create your models here.

class Task(models.Model):
  status_choices = [
    ('completed', 'completed'),
    ('pending', 'pending'),
    ('inprogress','inprogress')
  ]
  title = models.CharField(max_length=50,blank=False)
  status = models.CharField(max_length=10, choices=status_choices,default='pending')
  username = models.CharField(max_length=10)
  assignedto = models.CharField(max_length=10)
  comment = models.CharField(max_length=50,default="",blank=True)
  parent = models.IntegerField(default=0)
  description= models.CharField(max_length=500,default="",blank=True)

  def __str__(self):
    return self.title

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
  role_choices = [
    ('teamlead', 'teamlead'),
    ('employee', 'employee'),
    ('manager', 'manager')
  ]
  username_id = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
  role = models.CharField(max_length=30, blank=False,choices=role_choices)

class Employee(models.Model):
  username_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
  lead = models.CharField(max_length=30, blank=False)

class images(models.Model):
  user_id = models.IntegerField()
  link = models.CharField(max_length=200)



