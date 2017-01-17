import datetime

from m2agro.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from produtos.models import Produto
from produtos.serializers import ProdutoSerializer, PrecoMedioSerializer, PrecoMedioMensalSerializer
from servicos.models import Servico

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def preco_medio(mes, ano):
    """
    Calcula o preco medio dos produtos utilizados nos servicos do mes.
    """
    # recupera todos os servicos filtrados por mes e ano
    servicos = Servico.objects.filter(data_inicio__month=mes, data_inicio__year=ano)

    total_preco = {}
    total_produto = {}

    # Interage com cada servico
    # Armazena num dicionario
    # total de preco e total de produtos
    for s in servicos.iterator():
        # recupera todos os valores gastos com o servico
        valores = s.valores_set.all()
        for v in valores.iterator():
            # faz a soma do preco e quantidade de cada produto
            total_preco[v.produto.nome] = total_preco.get(v.produto.nome, 0) + v.preco
            total_produto[v.produto.nome] = total_produto.get(v.produto.nome, 0) + v.quantidade

    # Calcula o preco medio de cada produto
    # e salva novo preco medio no modelo
    for k,v in total_preco.items():
        produto = get_object_or_404(Produto, nome=k)
        preco_medio = total_preco[k] / total_produto[k]
        produto.preco_medio = preco_medio
        produto.save()


class PrecoMedioUpdate(APIView):
    """
    List all, or update all.
    """

    renderer_classes = (JSONRenderer, )
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        # Podemos realizar filtos no resultado de produtos
        produtos = Produto.objects.filter(is_active=True)
        serializer = PrecoMedioSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrecoMedioMensalSerializer(data=request.data)
        if serializer.is_valid():
            mes = serializer.data.get('mes')
            ano = serializer.data.get('ano')
            preco_medio(mes, ano)
            return self.get(self,request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProdutosList(APIView):
    """
    List all, or create a new one.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)

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