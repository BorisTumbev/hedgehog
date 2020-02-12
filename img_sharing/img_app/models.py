from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    follows = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Post(models.Model):

    image_caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/', default='static/images/default.png')
    likes = models.ManyToManyField(Profile, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
