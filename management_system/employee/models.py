
from django.db import models

# Create your models here.
class Employe(models.Model):
    Empid = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=200)
    Birthdate = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Adress = models.CharField(max_length=200)
    Position = models.CharField(max_length=100)
    Salary = models.CharField(max_length=100)
    Phone = models.CharField(max_length=50)
