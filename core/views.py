from django.shortcuts import render
from .models import Arte
from .models import Usuario
from .models import Imagens
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	Artes = Arte.objects.all().order_by('-id')[:3]
	return render(request, 'index.html')

def resultadobuscar(request):
	
	if request.method == 'GET':
		if 'nomeget' in request.GET:
			nomeget=request.GET.get("nomeget")
		else: 
			nomeget=""
		artes =  Arte.objects.filter(descricao__icontains=nomeget)
	else:
		artes = Arte.objects.all()

	context = {
		'artes': artes
	}

	return render(request, 'ResultadoBuscar.html', context) 

def arte_detalhes(request):

	Artes = Arte.objects.all()
	context = {
	'Artes': Artes
	}
	return render(request,'arte_detalhes.html', context)


def gerenciararte(request):
	artes = Arte.objects.all()
	imagens = Imagens.objects.all()
	usuario = Usuario.objects.all()
	context = {
		'artes': artes,
		'imagens':imagens,
		'usuario': usuario,

	}

	return render(request, 'gerenciararte.html', context)

