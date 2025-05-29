from django.shortcuts import render

# Create your views here.

def turma(request):
    return render (request, 'turma/listartTurmas.html')
def turmas(request):
    return render (request, 'turmas/listartTurmas.html')
def lista(request):
    return render (request, 'lista/listartTurmas.html')
#def msgturma(request):
    #t_html = '<html><title>Django - Exercícios</title><div class="collapse navbar-collapse justify-content-end" id="mynavbar"><div class="navbar-nav"><a href="../escola.html" class="nav-link">Início</a><a href="cadastroAluno.html" class="nav-link">Cadastrar</a><a href="listarAlunos.html" class="nav-link">Listar</a></div></div></html>'
    #return HttpResponse(t_html)
