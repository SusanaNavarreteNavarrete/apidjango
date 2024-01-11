"""APIDJANGO9ISC22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from api.views import ComponentDetailView, Graficas, Home, LoginView, descargar_archivo
from api.views import Login
from api.views import Form
from api.views import Inicio
from api.views import ProcesarRegistroView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('login.html',Login.as_view(),name='login'),
    path('form.html',Form.as_view(),name='form'),
    path('inicio.html',Inicio.as_view(),name='inicio'),
    path('login/', LoginView.as_view(), name='loginview'),
    path('procesar_registro/', ProcesarRegistroView.as_view(), name='procesar_registro'),
    path('graficas/', Graficas.as_view(), name='graficas'),
    path('componente/<str:component_name>/', ComponentDetailView.as_view(), name='component_detail'),
]
  