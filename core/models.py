from distutils.command.upload import upload
from django.db import models
from attractions.models import Atracao
from comments.models import Comentario
from evaluation.models import Avaliacao
from address.models import Endereco


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Atracao)
    comment = models.ManyToManyField(Comentario)
    evaluation = models.ManyToManyField(Avaliacao)
    address = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.name