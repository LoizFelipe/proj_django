from django.urls import path

from . import views

urlpatterns = [
    path('msg_do_aluno/', views.msg_do_aluno, name="msg_do_aluno"),
    #path('msg_do_aluno_render/', views.msg_do_aluno_render, name="msg_do_aluno_render"),

]