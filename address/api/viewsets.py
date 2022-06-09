from http.client import ImproperConnectionState
from rest_framework import viewsets
from address.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer