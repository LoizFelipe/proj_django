from django.shortcuts import HttpResponse , render

# Create your views here.
def index(request):
    return HttpResponse("Ola! eu sou o index. (por a Logo ?)")

def exibe_mensagem(request):
    t_html = '<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>ABC SPORT</title><link rel="icon" href="https://img.freepik.com/vetores-premium/castelo-simples-no-estilo-pixel-art_475147-1136.jpg?w=2000" type="image/x-icon"></head><body><p> Esta é minha pagina de indice </p></body></html>'
    return HttpResponse(t_html)

'<html><body>OlaOla</body></html>'
def portuga(request):
    t_html = '<html><body>Dentro do (tipos de atividade)</body></html>'
    return HttpResponse(t_html)

def testrender(request):
    
    return render(request,'escola.html')

def msg_do_aluno_render(request):
    
    return render(request,'escola.html')



#def aluno(request):
    #t_html = '<html><body>Dentro do ? (sou aluno luiz)</body></html>'
    #return HttpResponse(t_html)

