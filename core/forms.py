from django import forms
from django.forms import ModelForm
from .models import Usuario
from .models import Arte
from .models import Categoria
from .models import cartaoCredito

class autenticacao(forms.Form):
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())
	def __init__(self, arg):
		super(au, self).__init__()
		self.arg = arg

class UsuarioModelForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ['nome', 'sobrenome', 'cpfCnpj' , 'email', 'senha']

class ArteModelForm(forms.ModelForm):
    class Meta:
        model = Arte
        fields = '__all__'

class EditArteModelForm(forms.ModelForm):
	class Meta:
		model = Arte
		fields = ['descricao', 'preco']

class CartaoModelForm(forms.ModelForm):	
	class Meta:
		model = cartaoCredito
		fields = ['numero', 'codSeguranca', 'nomeCartao', 'dataValidade']
