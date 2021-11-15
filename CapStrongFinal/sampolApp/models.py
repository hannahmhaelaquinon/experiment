from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import AutoField
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class Register(models.Model):
    student_id = models.AutoField(primary_key = True)
    sName = models.CharField(max_length = 255)
    plateNum = models.IntegerField()
    idNum = models.IntegerField()
    vType = models.CharField(max_length = 1000)
    

    class meta:
        db_table = 'Register'
    def __str__(self):
        return self.student_id

class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    Fname = models.CharField(max_length=50, null=True)
    Lname = models.CharField(max_length=50, null=True)
    Email = models.CharField(max_length=50, null=True)
    Uname = models.CharField(max_length=50, null=True)
    Pass = models.CharField(max_length=50, null=True)
    

    class meta:
        db_table = 'User'