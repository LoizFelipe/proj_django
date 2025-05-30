from django.urls import path
from . import views

app_name = 'tiposdeatividade'

urlpatterns = [
    path('listar', views.listar, name='listar'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
       
    
]