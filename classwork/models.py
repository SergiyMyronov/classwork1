from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    header = models.CharField(max_length=200)
    short_description = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.header


class Comment(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
