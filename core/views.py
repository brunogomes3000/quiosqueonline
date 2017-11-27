from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def resultadobuscar(request):
	return render(request, 'ResultadoBuscar.html')

