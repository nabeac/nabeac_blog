from django.db import models
from account.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    creat_date = models.DateTimeField(auto_now_add=True)
    updat_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
