from django.urls import path
from . import views

app_name = 'utilitarios'

urlpatterns = [
    path('cadastro', views.cadastrar, name="cadastrar"),
    path('carga/', views.popular_bd, name='popular'),
]
