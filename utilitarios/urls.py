from django.urls import path

from . import views

urlpatterns = [
    path('msgutilitarios/', views.msgutilitarios, name="msgutilitarios"),
    
]