from django.db import models
from mysite.settings import DBNAME
from djangotoolbox.fields import ListField

# MY MODELS

class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    time = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    food_provided = models.CharField(max_length=30)