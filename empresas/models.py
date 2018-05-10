from django.db import models

class Empresa(models.Model):

	razao_social = models.CharField(max_length=255)
	telefone = models.CharField(max_length=15)
	quantidade_de_devs = models.CharField(max_length=15)
	classificacao = models.CharField(max_length=255, null=True)