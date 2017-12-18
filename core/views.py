from django.shortcuts import render
from .models import Arte
from .models import Usuario
from .models import Categoria
from .forms import CartaoModelForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioModelForm
from .forms import ArteModelForm
from .forms import EditArteModelForm
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


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
	lista_artes = req.session['artes']
	total = 0
	for arte in lista_artes:
		total += arte[2]
	return total

def finalizarcompra(request):
	form = CartaoModelForm(request.POST or None)
	context = {
		'form': form,
	}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('/finalizarcompra')
	return render(request, 'finalizarcompra.html', context)

def editdadospessoais(request):
	return render(request, 'editdadospessoais.html')

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
		return redirect('/gerenciararte')
	context = {
		'formEditArte': formEditArte,
		'arte': arte,
	}
	return render(request, 'editarte.html', context)

def removerarte(request):
	if request.method == 'GET':
		id_arte = request.GET.get("id")
		arte = Arte.objects.get(id = id_arte)
		arte.delete()
	context = {
		'arte': arte,
	}
	return render(request, 'gerenciararte.html', context)

def enviarArte(request):
	if request.method == 'POST':
		formArte = ArteModelForm(request.POST, request.FILES)
		if formArte.is_valid():
			arte = formArte.save(commit=False)
			arte.save()
			return redirect('/gerenciararte')

	formArte = ArteModelForm()
	context = {
		'formArte' : formArte,

	}
	return render( request, 'enviarArte.html', context)

def usuario(request):
	return render( request, 'usuario.html')



@login_required(login_url='login')
def usuario (request):
	return render(request, 'usuario.html')

def sobre(request):
	return render( request, 'sobre.html')
