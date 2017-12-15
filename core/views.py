from django.shortcuts import render
from .models import Arte
from .models import Usuario
from .models import Imagens
from .models import Categoria
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioModelForm
from .forms import ArteModelForm
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect


# Create your views here.
def index(request):
	Artes = Arte.objects.all().order_by('-id')[:3]

	form = UserCreationForm (request.POST or None)
	form2 = UsuarioModelForm(request.POST or None)

	context = {
		'form': form,
		'form2': form2,

	}

	if request.method == 'POST':
		if form.is_valid():
			user_post = UserCreationForm(request.POST)
			user = user_post.save(commit=False)
			user.set_password(user_post.cleaned_data['password'])
			user.save()
			if form2.is_valid():
				usuario_post = UsuarioModelForm(request.POST)
				usuario = usuario_post.save(commit=False)
				usuario.user = user
				usuario.save()
			return redirect('/index')
			form.save()



	return render (request, 'index.html', context)


def resultadobuscar(request):
	categoria = Categoria.objects.all()
	imagens = Imagens.objects.all()
	page = request.GET.get('page', 1)


	if request.method == 'GET':
		if 'nomeget' in request.GET:
			nomeget=request.GET.get("nomeget")
		else:
			nomeget=""
		if 'categoriaget' in request.GET and request.GET.get("categoriaget")!="Escolha a categoria":
			categoriaget=request.GET.get("categoriaget")
		else:
			categoriaget=Categoria.objects.values_list('id')

		artest =  Arte.objects.filter(descricao__icontains=nomeget, categoria__id__in=categoriaget)


		paginator = Paginator(artest, 8)
	else:
		artest = Arte.objects.all()
		paginator = Paginator(artest, 8)
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
	artes = Arte.objects.get(id = id_arte)
	context = {
	'artes': artes
	}
	return render(request,'arte_detalhes.html', context)



def gerenciararte(request):
	artes = Arte.objects.all()
	imagens = Imagens.objects.all()
	usuario = Usuario.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(artes, 8)

	try:
		artes = paginator.page(page)
	except 	PageNotAnInteger:
		artes = paginator.page(1)
	except EmptyPage:
		artes = paginator.page(paginator.num_pages)

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

def finalizarcompra(request):
	return render(request, 'finalizarcompra.html')

def editdadospessoais(request):
	return render(request, 'editdadospessoais.html')

def editarte(request):
	id_arte = request.GET.get("id")
	arte = Arte.objects.get(id=id_arte)
	context = {
		'arte': arte
	}
	return render(request, 'editarte.html', context)

def enviarArte(request):
	formArte = ArteModelForm(request.POST or None)
	context = {
	'formArte' : formArte
	}
	if request.method == 'POST':
		if formArte.is_valid():
			arte_post = ArteModelForm(request.POST)
			arte = arte_post.save(commit=False)
			arte.save()
			return redirect('/gerenciararte')
	return render( request, 'enviarArte.html', context)

def usuario(request):
	return render( request, 'usuario.html')


@login_required(login_url='login')
def usuario (request):
	return render(request, 'usuario.html')

def sobre(request):
	return render( request, 'sobre.html')
