from django.db import models

from django.db import models


class Admin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    private_key=models.CharField(max_length=100)

class Training(models.Model):
    training=models.CharField(max_length=1000)

class Chapter(models.Model):
    chapter=models.CharField(max_length=100)
    
class Blogs(models.Model):
    chapter=models.CharField(max_length=100)
    page_number=models.CharField(max_length=100)
    blog=models.CharField(max_length=50000)
