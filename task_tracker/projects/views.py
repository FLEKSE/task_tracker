from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import CustomUser, Project, Task
from .forms import ProjectForm, TaskForm
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('projects')

    def form_valid(self, form):
        messages.success(self.request, "Добро пожаловать!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Неверные учетные данные")
        return super().form_invalid(form)


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = CustomUser.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Регистрация успешна!")
        return redirect("register")


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

@login_required
def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
def change_project_status(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        project.status = new_status
        project.save()
        return redirect('projects')
@login_required
def task_view(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'task.html', {'tasks': tasks, 'project': project})


@login_required
def change_task_status(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        return redirect('task_view', project_id=task.project.project_id)
    return redirect('task_view', project_id=task.project.project_id)

@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_view', project_id=project.project_id)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form, 'project': project})