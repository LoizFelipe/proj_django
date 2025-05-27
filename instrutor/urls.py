from django.urls import path

from . import views

app_name = 'instrutor'

urlpatterns = [
    path('instru', views.instar, name='instar'),    
    
    
]