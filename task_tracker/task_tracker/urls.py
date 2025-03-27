from django.contrib import admin
from django.urls import path, include
from projects.views import CustomLoginView, RegisterView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('projects/', include('projects.urls')),
]