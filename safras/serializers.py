from rest_framework import serializers

from safras.models import Safra


class SafraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Safra
        fields = ('pk', 'nome', 'data_inicio', 'data_fim')