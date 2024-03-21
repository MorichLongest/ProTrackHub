# models.py
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.heading

