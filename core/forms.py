from django import forms
from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Usuario

class autenticacao(forms.Form):
	email = forms.CharField()
	senha = forms.CharField(widget=forms.PasswordInput())
	def __init__(self, arg):
		super(au, self).__init__()
		self.arg = arg


class UsuarioModelForm(forms.ModelForm):	

	class Meta:
		model = Usuario
		fields = ['nome', 'sobrenome', 'cpfCpnj' , 'email', 'senha']