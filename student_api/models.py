from django.db import models

# Create your models here.

class student1(models.Model):
    name = models.CharField(max_length = 20)
    uname = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 10)
    dob = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    address = models.CharField(max_length = 60)