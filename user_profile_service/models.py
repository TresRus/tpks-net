from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nqme = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    post = models.CharField(max_length=60)
    home_phonenumber = models.CharField(max_length=30)
    mobile_phonenumber = models.CharField(max_length=30)
    workspace_address = models.CharField(max_length=200)


