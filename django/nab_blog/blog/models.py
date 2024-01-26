from django.db import models
# from account.models import User
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    c_data = models.DateTimeField(auto_now=True)
    u_data = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
