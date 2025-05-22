from django.shortcuts import HttpResponse

# Create your views here.

def msgturma(request):
    t_html = '<html><body>Dentro da turma (turma bala de fuzil)</body></html>'
    return HttpResponse(t_html)
