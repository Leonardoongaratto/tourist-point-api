from dataclasses import field
from rest_framework import serializers
from comments.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'user', 'comment', 'date', 'approved']