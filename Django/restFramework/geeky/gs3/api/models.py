from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    roll = models.IntegerField()
    addr = models.CharField(max_length=60)
