"""
URL configuration for noesis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Página principal
    path('admin/', admin.site.urls),  # Django Admin
    path('admin-app/', include('app_db.urls.urls_admin')),  # Rutas del Administrador de tu aplicación
    path('empleado/', include('app_db.urls.urls_empleado')),  # Rutas para el Empleado
    path('auditor/', include('app_db.urls.urls_auditor')),  # Rutas para el Auditor
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Vista de inicio de sesión
    path('logout/', LogoutView.as_view(), name='logout'),  # Vista de cierre de sesión
]

