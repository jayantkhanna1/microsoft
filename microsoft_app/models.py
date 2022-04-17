from django.db import models

from django.db import models


class Admin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    private_key=models.CharField(max_length=100)

class Training(models.Model):
    training=models.CharField(max_length=1000)