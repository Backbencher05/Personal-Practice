from django.db import models
from django.db.models.base import Model

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)
    

    def __str__(self):
        return self.ename

class Jobmodel(models.Model):
    posting_date = models.DateField()
    location = models.CharField(max_length=64)
    offered_salary = models.IntegerField()
    Qualification  = models.IntegerField()



class Books(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    published_date = models.DateField()

class Costomer(models.Model):
    name = models.CharField(max_length=64)
    c_no = models.IntegerField()
    mail_id = models.EmailField()
    phone_no = models.IntegerField()
    age = models.IntegerField()