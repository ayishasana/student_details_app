from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_adm=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)

class Student(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_pic= models.FileField(upload_to='profilepic/')
    dob = models.DateField(max_length=8)
    mobile = models.CharField(max_length=10)

    @property
    def age(self):
        return int((datetime.now().date() - self.dob).days / 365.25)


    def __str__(self):
        return self.name

class admregister(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    mark = models.IntegerField()



