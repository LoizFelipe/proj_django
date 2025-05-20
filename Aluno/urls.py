from django.urls import path

from . import views

urlpatterns = [
    path('msg_do_aluno/', views.msg_do_aluno, name="msg_do_aluno"),

]