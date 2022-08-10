from statistics import mode
from django.db import models

# Create your models here.
class checklog( models.Model):
    firstname = models.CharField( max_length=100)
    lastname = models.CharField( max_length=100)
    address = models.TextField()
    phoneno = models.IntegerField()
    password = models.TextField()
    