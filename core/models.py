from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class cartaoCredito(models.Model):
    numero = models.CharField('Número de cartão', max_length=16, blank=True, null=True)
    codSeguranca = models.CharField('Código de segurança', max_length=3, null=True)
    nomeCartao = models.CharField('Nome', max_length=40, null=True)
    dataValidade = models.DateField('Data Vencimento')


class Usuario(models.Model):
    cpfCnpj = models.CharField('CPF', max_length=11, null=True)
    cartao = models.ManyToManyField(cartaoCredito, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.cpfCnpj

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Categoria(models.Model):
    categoria = models.CharField("Categoria da arte", max_length=20, null=True)

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Arte(models.Model):
    descricao = models.CharField("Descrição", max_length=100, blank=True, null=True)
    dataCadastro = models.DateField('Data de cadastro', auto_now_add=True)
    email = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    preco = models.FloatField("Preço", blank=True, null=True)
    imagem_principal = models.ImageField(upload_to='img/imagensArtes/', verbose_name='Imagem da Arte', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Arte'
        verbose_name_plural = 'Artes'
