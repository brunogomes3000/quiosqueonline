from django.db import models


class Usuario(models.Model):
    email = models.CharField('E-mail', primary_key=True, max_length=30)
    senha = models.CharField('Senha', max_length=16, null=True)
    cpfCpnj = models.CharField('CPF', max_length=11, null=True)

    def __str__(self):
        return self.email


class Arte(models.Model):
    descricao = models.CharField("Descrição", max_length=100, null=True)
    dataCadastro = models.DateField('Data de cadastro', auto_now_add=True)
    email = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Arte'
        verbose_name_plural = 'Artes'


class Imagens(models.Model):
    dataImagem = models.DateTimeField("Data da imagem", auto_now_add=True)
    descricao = models.CharField("Descrição", max_length=100, null=True)
    idArte = models.ForeignKey(Arte, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
