from django.urls import path
from .views import projects_view, task_view, change_task_status, change_project_status, create_project, create_task, task_detail

urlpatterns = [
    path('', projects_view, name='projects'),
    path('tasks/<int:project_id>', task_view, name='task_view'),
    path('tasks/change_status/<int:task_id>/', change_task_status, name='change_task_status'),
    path('change_status/<int:project_id>/', change_project_status, name='change_project_status'),
    path('create_project/', create_project, name='create_project'),
    path('create_task/<int:project_id>/', create_task, name='create_task'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
]
