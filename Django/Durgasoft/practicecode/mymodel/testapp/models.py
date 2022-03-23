from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    name = models.CharField(max_length=52)
    esal = models.IntegerField()
    eaddr = models.CharField(max_length=85)


    def __str__(self):
        return self.name
