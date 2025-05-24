from django.urls import path

from . import views

urlpatterns = [
    path('msgdomarcao/', views.msgdomarcao, name="msgdomarcao"),    
    path('msgdomarcao_render/', views.msgdomarcao_render, name="msgdomarcao_render"),
    
]