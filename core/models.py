from django.db import models

class Usuario(models.Model):
	email= models.CharField('E-mail',primary_key=True, max_length=30)
	senha= models.CharField('Senha', max_length=16)
	cpfCpnj= models.CharField('CPF', max_length=11)
	
	def __str__(self):
		return self.email