from statistics import mode
from django.db import models

# Create your models here.
class Logform( models.Model):
    firstname = models.CharField( max_length=40)
    lastname = models.CharField( max_length=40)
    address = models.TextField( max_length=100)
    phoneno=models.IntegerField()
    password = models.TextField( max_length=34)

