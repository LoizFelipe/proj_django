from django.urls import path
from . import views

app_name = 'titulos'

urlpatterns = [
    path('titulo', views.titulo, name="titulo"),
]