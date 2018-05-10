from rest_framework.generics import ListCreateAPIView
from .models import Empresa
from .serializer import EmpresaSerializer
from django.http import HttpResponse
import json

class EmpresaListView(ListCreateAPIView):

	serializer_class = EmpresaSerializer

	def get_queryset(self, *args, **kwargs):

		return Empresa.objects.all()
		#permission_classes = ()

	def perform_create(self, serializer):
		
		serializer.save()