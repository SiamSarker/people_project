from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
