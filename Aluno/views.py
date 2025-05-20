from django.shortcuts import HttpResponse

# Create your views here.

def msg_do_aluno(request):
    t_html = '<html><body>Dentro do ? (sou aluno luiz)</body></html>'
    return HttpResponse(t_html)

