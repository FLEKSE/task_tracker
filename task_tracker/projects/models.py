from django.db import models
from django.contrib.auth.models import AbstractUser


class Project(models.Model):
    STATUS_CHOICES = [
        ('in_process', 'В процессе'),
        ('paused', 'Приостановлен'),
        ('finished', 'Завершен'),
        ('on_check', 'На проверке'),
        ('canceled', 'Отменен')
    ]
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    creating_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='in_process')
    finish_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('analysis', 'Анализируется'),
        ('in_process', 'В работе'),
        ('canceled', 'Отменена'),
        ('completed', 'Выполнена'),
        ('paused', 'Приостановлена')
    ]
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    creating_date = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField('CustomUser', related_name='tasks')
    status = models.CharField(choices=STATUS_CHOICES, default='created')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_name


class UnderTask(models.Model):
    under_task_id = models.AutoField(primary_key=True)
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='under_task', null=True, blank=True)
    status = models.BooleanField()  # передать True или False для добавления галочки

    def __str__(self):
        return f"UnderTask {self.under_task_id} for {self.task.task_name}"


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('developer', 'Developer'),
    ]

    projects = models.ManyToManyField(Project, related_name='users', blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True,
        help_text="Specific permissions for this user."
    )

    def __str__(self):
        return self.username



