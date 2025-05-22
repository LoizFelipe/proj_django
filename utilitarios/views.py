from django.shortcuts import HttpResponse

# Create your views here.

def msgutilitarios(request):
    t_html = '<html><body>Dentro do utilidades</body></html>'
    return HttpResponse(t_html)
