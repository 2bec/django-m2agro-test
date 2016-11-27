from rest_framework import serializers

from servicos.models import Servico, Valores
from produtos.models import Produto
from safras.models import Safra
from produtos.serializers import ProdutoSerializer
from safras.serializers import SafraSerializer


class ValorSerializer(serializers.ModelSerializer):

    produto = ProdutoSerializer()
    
    class Meta:
        model = Valores
        fields = ('produto','data_compra', 'preco', 'quantidade')


class ServicoSerializer(serializers.ModelSerializer):

    safra = SafraSerializer()
    produtos = ValorSerializer(many=True, source='valores_set')

    class Meta:
        model = Servico
        fields = ('pk', 'nome', 'safra', 'data_inicio', 'data_fim', 'produtos')

    def create(self, validated_data):
        valores_data = validated_data.pop('valores_set')
        safra_data = validated_data.pop('safra')
        safra, created = Safra.objects.get_or_create(**safra_data)
        servico = Servico.objects.create(safra=safra, **validated_data)
        for valor_data in valores_data:
            produto_data = valor_data.pop('produto')
            produto, created = Produto.objects.get_or_create(**produto_data)
            Valores.objects.create(servico=servico, produto=produto, **valor_data)
        return servico