from django.db import models

# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=500,default=None)
    email=models.EmailField(default=None)
    password=models.CharField(max_length=500)
    name=models.CharField(max_length=500,default=None)
