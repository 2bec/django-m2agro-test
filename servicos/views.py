from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from servicos.models import Servico, Valores
from servicos.serializers import ServicoSerializer, ValorSerializer


class ServicosList(APIView):
    """
    List all, or create a new one.
    """
    def get(self, request, format="xml"):
    	# Podemos realizar filtos no resultado de servicos
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicoDetail(APIView):
    """
    Retrieve, update or delete a instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Servico, pk=pk)

    def get(self, request, pk, format=None):
        servico = self.get_object(pk)
        serializer = ServicoSerializer(servico)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        servico = self.get_object(pk)
        serializer = ServicoSerializer(servico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        servico = self.get_object(pk)
        servico.delete()
        return Response(servico)