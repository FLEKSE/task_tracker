from django import forms
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status', 'finish_date']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'status']