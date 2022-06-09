from dataclasses import fields
from rest_framework import serializers
from evaluation.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id','user', 'comment', 'note', 'date']