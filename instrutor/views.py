from django.shortcuts import render

# Create your views here.

#def msgdomarcao(request):
    #t_html = '<html><body>Dentro do instrutor(MARCÃoO) (tipos de atividade)</body></html>'
    #return HttpResponse(t_html)

def msgdomarcao_render(request):
    t_html = '<html><body>Dentro do instrutor(MARCÃoO) render (tipos de atividade)</body></html>'
    return render(request,'escola.t_html')



