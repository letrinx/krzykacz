from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tweet(models.Model):
    content = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_DEFAULT, default="Anonymous"
    )

