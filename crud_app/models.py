from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
# Create your models here.
