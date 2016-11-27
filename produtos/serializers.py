from rest_framework import serializers

from produtos.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('pk', 'nome', 'preco_medio', 'created', 'updated',"is_active")