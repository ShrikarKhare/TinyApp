from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass
class Users(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=100)

class Url(models.Model):
    short_url = models.URLField(max_length=10)
    long_url = models.URLField(max_length=256)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()

