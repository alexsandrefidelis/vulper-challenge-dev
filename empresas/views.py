from rest_framework.generics import ListCreateAPIView
from .models import Empresa
from .serializer import EmpresaSerializer, EmpresaListSerializer
from django.http import HttpResponse
import json

class EmpresaListView(ListCreateAPIView):

	serializer_class = EmpresaListSerializer

	def get_queryset(self, *args, **kwargs):

		return Empresa.objects.all()
		#permission_classes = ()

class EmpresaSendView(ListCreateAPIView):

	serializer_class = EmpresaSerializer

	def perform_create(self, serializer):

		serializer.save()