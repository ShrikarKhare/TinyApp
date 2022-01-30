from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

class User(AbstractUser):
    pass
class Users(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
        
class Url(models.Model):
    short_url = models.URLField(max_length=10)
    long_url = models.URLField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    slug = models.SlugField(unique=True, max_length=256)

    def __str__(self):
        return self.short_url

    def get_absolute_url(self):
       return reverse('urls_detail', args=[str(self.pk)])