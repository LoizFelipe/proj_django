from django.shortcuts import HttpResponse

# Create your views here.

def msg_do_aluno(request):
    t_html = '<html><body>Dentro do ? (sou aluno luiz)</body></html>'
    return HttpResponse(t_html)

#def msg_do_aluno_render(request):
    #t_html = '<html><body>Dentro do aluno render (sou aluno luiz)</body></html>'
    #return render(request,'escola.t_html')


