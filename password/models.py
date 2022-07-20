from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Password(models.Model):
    host = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    passwrd = models.CharField(max_length=201)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passwords')
