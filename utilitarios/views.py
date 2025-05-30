from django.shortcuts import render

# Create your views here.

def cadastrar(request):
    return render (request, 'utilitarios/contato.html')