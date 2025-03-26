from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    # project_id = models.ManyToManyField()


class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    creating_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    finish_date = models.DateTimeField()


class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    task_name = models.CharField()
    creating_date = models.DateTimeField()
    # user_id = models.ManyToManyField()
    status = models.CharField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    finish_date = models.DateTimeField()


class UnderTask(models.Model):
    under_task_id = models.IntegerField(primary_key=True)
    text = models.CharField()
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField()
