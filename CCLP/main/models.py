from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(default = "", max_length=255)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 

class Person(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    section = models.ForeignKey(Class, on_delete = models.CASCADE)
    teacher = models.ForeignKey(User, on_delete = models.CASCADE)
    points = models.IntegerField(default=0)
    description = models.CharField(max_length = 255)

