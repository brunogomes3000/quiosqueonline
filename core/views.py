from django.shortcuts import render
from .models import Arte
from .models import Usuario
from .models import Imagens
from .models import Categoria
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	Artes = Arte.objects.all().order_by('-id')[:3]
	return render(request, 'index.html')

def resultadobuscar(request):
	categoria = Categoria.objects.all()
	imagens = Imagens.objects.all()
	page = request.GET.get('page', 1)


	if request.method == 'GET':
		if 'nomeget' in request.GET:
			nomeget=request.GET.get("nomeget")
		else:
			nomeget=""
		if 'categoriaget' in request.GET and request.GET.get("categoriaget")!="":
			categoriaget=request.GET.get("categoriaget")
		else:
			categoriaget=Categoria.objects.values_list('id')

		artest =  Arte.objects.filter(descricao__icontains=nomeget, categoria__id__in=categoriaget)
	#else:
		#artes = Arte.objects.all()

		paginator = Paginator(artest, 3)
	else:
		artest = Arte.objects.all()
		paginator = Paginator(artest, 3)
	try:
		artes = paginator.page(page)
	except 	PageNotAnInteger:
		artes = paginator.page(1)
	except EmptyPage:
		artes = paginator.page(paginator.num_pages)

		

	context = {
		'categoria': categoria,
		'artes': artes,
		'imagens': imagens,
	}

	return render(request, 'ResultadoBuscar.html', context) 

def arte_detalhes(request):
	id_arte = request.GET.get("id")
	Artes = Arte.objects.get(id = id_arte)
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

def carrinho(request):

	#puxar os produtos da sessão
	#consultar todos os produtos no banco
	#somar os valores de cada produto e salvar em uma variávei
	#jogar em contexto os produtos e o valor total
	return render(request, 'carrinho.html')

def checkDadosPessoais(request):
	return render(request, 'checkDadosPessoais.html')

def editarDadosPessoais(request):
	return render(request, 'editarDadosPessoais.html')

def editarArte(request):
	id_arte = request.GET.get("id")
	arte = Arte.objects.get(id=id_arte)
	context = {
		'arte': arte
	}
	return render(request, 'editarArte.html', context)

def enviarArte(request):
	categoria = Categoria.objects.all()
	page = request.GET.get('page', 1)


	if request.method == 'GET':
		if 'categoriaget' in request.GET and request.GET.get("categoriaget")!="":
			categoriaget=request.GET.get("categoriaget")
		else:
			categoriaget=Categoria.objects.values_list('id')
		

	context = {
		'categoria': categoria
	}

	return render(request, 'enviarArte.html', context)
