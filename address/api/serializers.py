from address.models import Endereco
from rest_framework import serializers

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude']