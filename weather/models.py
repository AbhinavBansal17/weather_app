from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.

class User(AbstractUser):
    location = models.TextField(default="Georgia")