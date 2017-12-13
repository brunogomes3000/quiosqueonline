from django import forms

class autenticacao(forms.Form):
	email = forms.charField()
	senha = forms.charField(widget=forms.passwordInput())
	def __init__(self, arg):
		super(au, self).__init__()
		self.arg = arg
