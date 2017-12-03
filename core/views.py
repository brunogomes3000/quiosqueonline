from django.shortcuts import render
from .models import Arte
from .models import Usuario
from .models import Imagens

# Create your views here.
def index(request):
	
	return render(request, 'index.html')

def resultadobuscar(request):
	Artes = Arte.objects.all()
	context = {
	'Artes': Artes
	}

	return render(request, 'ResultadoBuscar.html', context) 

def arte_detalhes(request):
	return render(request,'arte_detalhes.html')

def gerenciararte(request):
	artes = Arte.objects.all()
	context = {
		'artes': artes,
	}
	return render(request, 'gerenciararte.html', context)