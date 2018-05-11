from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Empresa
from rest_framework import serializers

class EmpresaSerializer(ModelSerializer):

	class Meta:
		model = Empresa
		fields = ['razao_social', 'telefone', 'quantidade_de_devs']


class EmpresaListSerializer(ModelSerializer):

	class Meta:
		model = Empresa
		fields = ['razao_social', 'telefone', 'quantidade_de_devs']


	def get_classificacao(self):
		classificacao = None

		if quantidade_de_devs < 10:
			classificacao = "Vollmir" 
		else:
			classificacao = "Asgard"
		return classificacao