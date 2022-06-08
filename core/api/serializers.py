from core.models import PontoTuristico
from rest_framework import serializers


class PontoTuristicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['url', 'id', 'name', 'description']