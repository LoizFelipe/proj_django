from django.urls import path

from . import views

urlpatterns = [
    path('msgtitulo/', views.msgtitulo, name="msgtitulo"),
]