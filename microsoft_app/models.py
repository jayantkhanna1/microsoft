from django.db import models

from django.db import models

class Feedback(models.Model):
    feedback=models.CharField(max_length=1000)
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=300)

class Admin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    private_key=models.CharField(max_length=100)

class Training(models.Model):
    training=models.CharField(max_length=1000)