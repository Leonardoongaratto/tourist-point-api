from django.db import models
from attractions.models import Atracao
from comments.models import Comentario
from assessments.models import Avaliacao


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Atracao)
    comment = models.ManyToManyField(Comentario)
    assesment = models.ManyToManyField(Avaliacao)


    def __str__(self):
        return self.name