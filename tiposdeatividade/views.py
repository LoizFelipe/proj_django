from django.shortcuts import HttpResponse , render

# Create your views here.


def cadastrar(request):
    
    return render(request,'tiposdeatividade/cadastroTiposAtividade.html')

def listar(request):
    
    return render(request,'tiposdeatividade/listarTiposAtividade.html')
