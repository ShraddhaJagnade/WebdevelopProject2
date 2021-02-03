from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=70)
    Department = models.CharField(max_length=50)
    Address = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)