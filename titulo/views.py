from django.shortcuts import render
from titulo.models import Titulo

# Create your views here.

def cadastrar(request):
    return render (request, 'titulo/cadastroTitulos.html')

def listar(request):

    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulo' : lista_titulos
    }

    return render (request, 'titulo/listarTitulos.html', contexto=contexto)

