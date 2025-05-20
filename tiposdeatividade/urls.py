from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exibe_mensagem/', views.exibe_mensagem, name="exibir_mensagem"),

    #path('Loiz/', views.exibe_mensagem, name="exibir_mensagem"),
    path('portuga/', views.portuga, name="portuga"),
    
    #path('aluno/', views.aluno, name="aluno"),
    path('testrender/', views.testrender, name="testrender"),


]