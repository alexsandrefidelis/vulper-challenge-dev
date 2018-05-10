from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Empresa

class EmpresaSerializer(ModelSerializer):

	#teste = SerializerMethodField()

	class Meta:
		model = Empresa
		fields = ['razao_social', 'telefone', 'quantidade_de_devs']


	def get_test(self):
		teste = None

		if self.quantidade_de_devs < 10:
			teste = "Vollmir" 
		else:
			teste = "Asgard"
		return teste