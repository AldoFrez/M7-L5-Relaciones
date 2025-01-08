

# Create your views here.
from django.shortcuts import render
from .models import Trabajador
#def index(request):
#    trabajadores = Trabajador.object.all()
#    return render(request, 'uno_a_uno/index.html', {'trabajadores': trabajadores})

def index(request):
    context = {
        "trabajadores": Trabajador.objects.all()
    }
    return render(request, 'uno_a_uno/index.html', context) # es lo mismo que la clave valor, se pasa como contexto