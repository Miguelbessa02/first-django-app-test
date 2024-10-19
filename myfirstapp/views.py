from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World!")

def pagina_inicial(request):
    return render(request, 'dj/pagina_inicial.html')


def pagina_inicial(request):
    return render(request, 'dj/pagina_inicial.html')

