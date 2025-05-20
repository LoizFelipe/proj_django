from django.urls import path

from . import views

urlpatterns = [
    path('msgdomarcao/', views.msgdomarcao, name="msgdomarcao"),
]