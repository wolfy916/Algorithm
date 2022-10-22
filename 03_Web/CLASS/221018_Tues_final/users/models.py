from django.db import models

# Create your models here.
from clubs.models import Club

class User(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    country = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    balance = models.IntegerField()
    image = models.ImageField(blank=True)
    clubs = models.ManyToManyField(Club, related_name='users')

