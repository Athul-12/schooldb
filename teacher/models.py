from django.db import models
from sc_admin.models import Teacher

# Create your models here.

class student(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete = models.SET_NULL, null = True)
    s_name = models.CharField(max_length = 20)                # charfield 20 = sql varchar 20
    s_uname = models.CharField(max_length = 25)
    s_gender = models.CharField(max_length = 10)
    s_dob = models.CharField(max_length = 20)
    s_password = models.CharField(max_length = 10)
    s_photo = models.ImageField(upload_to = 'student/')
    s_address = models.CharField(max_length = 60)