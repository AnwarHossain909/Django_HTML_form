from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50, null=True, blank=True)

    phone = models.CharField(max_length=20, null=True, blank=True)

    password = models.CharField(max_length=100, null=True, blank=True)

    checkbox = models.BooleanField(default=False)


def __str__(self):
    return f"{self.name}"