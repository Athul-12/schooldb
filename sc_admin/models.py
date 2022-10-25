from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length = 20)                # charfield 20 = sql varchar 20
    email = models.CharField(max_length = 25)
    qualification = models.CharField(max_length = 20)
    exp = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 10)
    dob = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    photo = models.ImageField(upload_to = 'teacher/')
    address = models.CharField(max_length = 60)

class AdminLogin(models.Model):
    admin_username =  models.CharField(max_length = 20)
    admin_password = models.CharField(max_length = 20)


