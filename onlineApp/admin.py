from django.contrib import admin
from .models import Course,MyUser
# Register your models here.

admin.site.register(Course)
# admin.site.register(MyUserManager)
admin.site.register(MyUser)

