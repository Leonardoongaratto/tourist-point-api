from attractions.models import Atracao
from rest_framework import serializers


class AtracaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'name', 'description', 'time_func', 'minimum_age']