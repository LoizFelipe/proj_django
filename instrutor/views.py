from django.shortcuts import render

# Create your views here.


def cadastrar(request):
    return render (request, 'instrutor/cadastroInstrutor.html')

def listar(request):
    return render (request, 'instrutor/listaInstrutor.html')

def listarnv(request):
    return render (request, 'instrutor/listarNV_Instrutores.html')




