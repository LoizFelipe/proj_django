from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('exibe_mensagem/', views.exibe_mensagem, name="exibir_mensagem"),
       
    #path('aluno/', views.aluno, name="aluno"),
    path('testrender/', views.testrender, name="testrender"),

    path('msg_do_aluno_render/', views.msg_do_aluno_render, name="msg_do_aluno_render"),
    
]