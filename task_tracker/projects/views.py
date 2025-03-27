from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Неверные учетные данные")
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = CustomUser.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Регистрация успешна!")
        return redirect("login")
    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "index.html", {"user": request.user})
