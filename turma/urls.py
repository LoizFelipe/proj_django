from django.urls import path

from . import views

urlpatterns = [
    path('msgturma/', views.msgturma, name="msgturma"),
]