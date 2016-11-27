from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer


def preco_medio(produto):
	"""
	Calcula o preco medio de um produto
	"""
	total = 0
	for v in produto.valores_set.all():
		total += v.preco
	n = produto.valores_set.all().count()
	return total / n


class ProdutosList(APIView):
    """
    List all, or create a new one.
    """
    def get(self, request, format=None):
        # Podemos realizar filtos no resultado de produtos
        produtos = Produto.objects.filter(is_active=True)
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdutoDetail(APIView):
    """
    Retrieve, update or delete a instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Produto, pk=pk)

    def get(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        produto = self.get_object(pk)
        produto.delete()
        return Response(produto)


    