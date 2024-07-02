from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=128, null=True, blank=True)

class Department(models.Model):
    title = models.CharField(max_length=32)
