from django.urls import path
from . import views

app_name = 'turmass'

urlpatterns = [
    #path('lista', views.listar, name='listar'),
    path('turma', views.turma, name="turma"),
    path('turmas', views.turmas, name="turmas"),
    path('lista', views.lista, name="lista"),

    
    
]