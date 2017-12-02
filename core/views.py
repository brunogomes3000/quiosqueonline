from django.shortcuts import render
from .models import Arte

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
	return render(request, 'gerenciararte.html')