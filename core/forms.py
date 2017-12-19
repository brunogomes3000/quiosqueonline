from django import forms
from django.forms import ModelForm
from .models import Usuario
from .models import Arte
from .models import Categoria
from .models import cartaoCredito
from django.contrib.auth.models import User

class autenticacao(forms.Form):
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())
	def __init__(self, arg):
		super(au, self).__init__()
		self.arg = arg

class UserModelForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username']

class UsuarioModelForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ['cpfCnpj']

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

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control mr-sm-2'
	    })
