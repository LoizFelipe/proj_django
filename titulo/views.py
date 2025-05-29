from django.shortcuts import render

# Create your views here.

def titulo(request):
    return render (request, 'titulo/tituloTitulo.html')
def lista(request):
    return render (request, 'titulo/listatTitulo.html')

