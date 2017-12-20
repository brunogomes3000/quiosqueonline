from django.shortcuts import render
from .models import Arte
from .models import Usuario
from .models import Categoria
from .forms import CartaoModelForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserModelForm
from .forms import UsuarioModelForm
from .forms import ArteModelForm
from .forms import EditArteModelForm
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
	Artes = Arte.objects.all().order_by('-id')[:3]


	formUser = UserModelForm(request.POST or None)
	formCPF = UsuarioModelForm(request.POST or None)
	form = UserCreationForm(request.POST or None)
	context = {
		'formUser': formUser,
		'formCPF': formCPF,
		'form': form
	}
	if request.method == 'POST':
		if form.is_valid() and formUser.is_valid():
			usuario_post = UserCreationForm(request.POST)
			usuario = usuario_post.save(commit=False)
			usuario.first_name = formUser.cleaned_data['first_name']
			usuario.last_name = formUser.cleaned_data['last_name']
			usuario.email = formUser.cleaned_data['email']
			usuario.save()
			if formCPF.is_valid():
				cpf_post = UsuarioModelForm(request.POST)
				cpf = cpf_post.save(commit=False)
				cpf.user  = usuario
				cpf.save()
	return render (request, 'index.html', context)


def resultadobuscar(request):
	categoria = Categoria.objects.all()
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


		paginator = Paginator(artest, 12)
	else:
		artest = Arte.objects.all()
		paginator = Paginator(artest, 12)
	try:
		artes = paginator.page(page)
	except 	PageNotAnInteger:
		artes = paginator.page(1)
	except EmptyPage:
		artes = paginator.page(paginator.num_pages)



	context = {
		'categoria': categoria,
		'artes': artes,
		'nomeget' : nomeget
	}

	return render(request, 'ResultadoBuscar.html', context)

def arte_detalhes(request):
	id_arte = request.GET.get("id")
	artes = Arte.objects.get(id = id_arte)
	context = {
	'artes': artes
	}
	return render(request,'arte_detalhes.html', context)


@login_required(login_url='login')
def gerenciararte(request):
	artes = Arte.objects.all()
	id_usuario = request.user
	usuario = Usuario.objects.get(user=id_usuario)
	page = request.GET.get('page', 1)
	paginator = Paginator(artes, 8)

	if request.method == 'GET':
		if 'op' in request.GET:
			if request.GET.get("op") == 'remover':
				if 'id' in request.GET:
					id_arte = request.GET.get("id")
					arte = Arte.objects.get(id = id_arte)
					arte.delete()

	try:
		artes = paginator.page(page)
	except 	PageNotAnInteger:
		artes = paginator.page(1)
	except EmptyPage:
		artes = paginator.page(paginator.num_pages)

	context = {
		'artes': artes,
		'usuario': usuario,

	}

	return render(request, 'gerenciararte.html', context)

def carrinho(request):

	lista_artes = []
	total = 0
	if 'artes' in request.session:
		lista_artes = request.session['artes']

	if request.method == 'GET':
		if 'op' in request.GET:
			if request.GET.get("op") == 'adicionar':
				if 'id' in request.GET:
					id_arte = request.GET.get("id")
					contador = 0
					for arte in lista_artes:
						if arte[0] == id_arte:
							return redirect('/carrinho')

					'''id_arte = request.GET.get("id")'''
					arte = Arte.objects.get(id=id_arte)
					lista_artes.append([id_arte, arte.descricao, arte.preco, arte.imagem_principal.url])
					request.session['artes'] = lista_artes
					return redirect('/carrinho?total={}'.format(totalCarrinho(request)))
			elif request.GET.get("op") == 'remover':
				if 'id' in request.GET:
					id_arte_remover = request.GET.get("id")
					cont = 0
					for arte in lista_artes:
						if arte[0] == id_arte_remover:
							del lista_artes[cont]
						cont+=1
					request.session['artes'] = lista_artes
					return redirect('/carrinho?total={}'.format(totalCarrinho(request)))
	total = totalCarrinho(request)
	context = {
		'total': total
	}
	return render(request, 'carrinho.html', context)


def totalCarrinho(req):
	if 'artes' in req.session:
		lista_artes = req.session['artes']
		total = 0
		for arte in lista_artes:
			total += arte[2]
	else:
		total = 0
	return total

def todasAsArtes(req):
	if 'artes' in req.session:
		lista_artes = req.session['artes']
	return lista_artes

@login_required(login_url='login')
def finalizarcompra(request):
	id_usuario = request.user
	usuario = Usuario.objects.get(user=id_usuario)
	form = CartaoModelForm(request.POST or None)
	lista_artes = todasAsArtes(request)
	vlTotal = totalCarrinho(request)
	nomesArtes = ""

	context = {
		'form': form,
		'usuario': usuario,
		'lista_artes': lista_artes,
		'vlTotal': vlTotal,
	}

	if request.method == 'POST':
		if form.is_valid():
			for artes in lista_artes:
				nomesArtes = nomesArtes + '\n- ' + artes[1]

			email = usuario.user.email
			nome = usuario.user.first_name
			nome2 = usuario.user.last_name
			mensagem_completa = 'Olá, {0} {1}!\nVocê acaba de adquirir em nosso site os direitos de uso da(s) seguinte(s) arte(s): \n\n{2}\n\nValor total: R$ {3} \n\n\nSe não foi você quem fez essa compra, quem sabe morre'.format(nome, nome2, nomesArtes, vlTotal)
			send_mail('Confirmação de compra | Quiosque Online', mensagem_completa, settings.DEFAULT_FROM_EMAIL, [email])
			cartao = form.save(commit=False)
			cartao.usuario = usuario
			cartao.save()
			return redirect('/gerenciararte')
	return render(request, 'finalizarcompra.html', context)

@login_required(login_url='login')
def editdadospessoais(request):
	id_usuario = request.user
	usuario = Usuario.objects.get(user=id_usuario)
	context = {
		'usuario': usuario,
	}
	return render(request, 'editdadospessoais.html', context)

@login_required(login_url='login')
def editarte(request):
	if request.method == 'POST':
		id_arte = request.POST.get("id")
		arte = Arte.objects.get(id = id_arte)
		formEditArte = EditArteModelForm(request.POST or None, instance = arte)
		if formEditArte.is_valid():
			arte.save()
			return redirect('/gerenciararte')
	formEditArte = EditArteModelForm()
	if request.method == 'GET':
		id_arte = request.GET.get("id")
		arte = Arte.objects.get(id = id_arte)
	context = {
		'formEditArte': formEditArte,
		'arte': arte,
	}
	return render(request, 'editarte.html', context)

@login_required(login_url='login')
def enviarArte(request):
	categorias = Categoria.objects.all()
	id_usuario = request.user
	usuario = Usuario.objects.get(user=id_usuario)

	if request.method == 'POST':
		formArte = ArteModelForm(request.POST, request.FILES)
		if formArte.is_valid():
			arte = formArte.save(commit=False)
			arte.usuario = usuario
			arte.save()
			return redirect('/gerenciararte')

	formArte = ArteModelForm()
	context = {
		'formArte' : formArte,
		'categorias' : categorias

	}
	return render( request, 'enviarArte.html', context)


@login_required(login_url='login')
def usuario (request):
	id_usuario = request.user
	usuario = Usuario.objects.get(user=id_usuario)
	context = {
		'usuario': usuario,
	}
	return render(request, 'usuario.html', context)

def sobre(request):
	return render( request, 'sobre.html')
