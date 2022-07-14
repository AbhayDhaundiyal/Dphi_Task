from ast import Pass
from django.db import models


class student(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.TextField()
    Password = models.TextField()
    is_std = models.BooleanField(default = True)

class Educator(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.TextField()
    Password = models.TextField()
    is_std = models.BooleanField(default = False)

class course(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.TextField()
    Desc = models.TextField()
    content = models.TextField()
    enrolled = models.ManyToManyField(student)
    creator = models.ForeignKey(Educator, on_delete=models.CASCADE)