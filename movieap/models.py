from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_names=models.CharField(max_length=30)
    actor_names=models.CharField(max_length=30)

