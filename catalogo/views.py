from django.shortcuts import render
from catalogo.models import Vilao

# Create your views here.

def mostrar_index(request):
    viloes = Vilao.objects.all()
    return render(request, 'index.html', {'viloes':viloes})

def mostrar_vilas(request):
    vilas = Vilao.objects.filter(categoria='Mana')
    return render(request, 'manas.html', {'vilas':vilas})
