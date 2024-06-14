from django.db import models


# Create your models here.
class Employee(models.Model):
    objects=None
    eid = models.IntegerField()
    name = models.CharField(max_length=21)
    email = models.EmailField()
    phone = models.IntegerField()
