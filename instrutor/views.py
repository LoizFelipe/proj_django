from django.shortcuts import HttpResponse , render

# Create your views here.

def msgdomarcao(request):
    t_html = '<html><body>Dentro do instrutor(MARCÃoO) (tipos de atividade)</body></html>'
    return HttpResponse(t_html)

def msgdomarcao_render(request):
    
    return render(request,'escola.html')



