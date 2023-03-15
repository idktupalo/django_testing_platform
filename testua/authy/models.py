from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField()