from django.shortcuts import render

# Create your views here.

def msgturma(request):
    t_html = '<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>ABC SPORT</title><link rel="icon" href="https://img.freepik.com/vetores-premium/castelo-simples-no-estilo-pixel-art_475147-1136.jpg?w=2000" type="image/x-icon"></head><body><p> Esta é minha pagina de teste render </p></body></html>'
    return render(t_html)
