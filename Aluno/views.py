from django.shortcuts import HttpResponse , render

# Create your views here.

def msg_do_aluno(request):
    t_html = '<html><body>Dentro do aluno (sou aluno Luiz)</body></html>'
    return HttpResponse(t_html)

def msg_do_aluno_render(request):
    return render(request,'escola.html')


