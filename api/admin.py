from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.

from .models import Task
from .models import Profile,Employee,images

admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Employee)
admin.site.register(images)