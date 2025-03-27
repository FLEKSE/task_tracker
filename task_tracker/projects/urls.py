from django.urls import path
from .views import projects_view, task_view, change_task_status

urlpatterns = [
    path('', projects_view, name='projects'),
    path('tasks/<int:project_id>', task_view, name='task_view'),
    path('tasks/change_status/<int:task_id>/', change_task_status, name='change_task_status'),
]
