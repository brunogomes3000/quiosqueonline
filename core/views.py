from django.shortcuts import render


# Create your views here.
def index(request):
	return render(request, 'index.html')

def resultadobuscar(request):
	if request.method == 'GET':
		if 'nomeget' in request.GET: 
			nomeget=request.GET.get("nomeget")
		else: nomeget="Arte não encontrada"

	return render(request, 'ResultadoBuscar.html')

def arte_detalhes(request):
	return render(request,'arte_detalhes.html')

