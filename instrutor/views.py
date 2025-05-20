from django.shortcuts import HttpResponse

# Create your views here.

def msgdomarcao(request):
    t_html = '<html><body>Dentro do instrutor(MARCÃoO) (tipos de atividade)</body></html>'
    return HttpResponse(t_html)
