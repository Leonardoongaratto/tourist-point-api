from core.models import PontoTuristico
from rest_framework import serializers
from attractions.api.serializers import AtracaoSerializer
from comments.api.serializers import ComentarioSerializer
from evaluation.api.serializers import AvaliacaoSerializer
from address.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(serializers.HyperlinkedModelSerializer):
    attraction = AtracaoSerializer(many=True, read_only=True)
    comment = ComentarioSerializer(many=True, read_only=True)
    evaluation = AvaliacaoSerializer(many=True, read_only=True)
    address = EnderecoSerializer()
    
    class Meta:
        model = PontoTuristico
        fields = [
            'id', 'name', 'description', 'picture',
            'attraction','comment', 'evaluation', 'address'
        ]