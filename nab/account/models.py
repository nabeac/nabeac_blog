from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=10,)
    birth = models.DateField(null=True, blank=True)
