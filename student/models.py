from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()

