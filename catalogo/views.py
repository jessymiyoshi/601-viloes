from django.shortcuts import render
from catalogo.models import Vilao

# Create your views here.

def mostrar_index(request):
    viloes = Vilao.objects.all()
    return render(request, 'index.html', {'viloes':viloes})