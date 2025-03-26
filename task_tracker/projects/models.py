from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    creating_date = models.DateTimeField()
    status = models.CharField(max_length=255)

