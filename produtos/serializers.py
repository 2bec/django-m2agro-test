from rest_framework import serializers

from produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('pk', 'nome', 'preco_medio', 'created', 'updated',"is_active")


class PrecoMedioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('nome', 'preco_medio', 'updated')

class PrecoMedioMensalSerializer(serializers.Serializer):
    mes = serializers.IntegerField()
    ano = serializers.IntegerField()