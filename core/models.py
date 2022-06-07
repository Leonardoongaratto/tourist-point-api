from django.db import models
from attractions.models import Atracao

class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attraction = models.ManyToManyField(Atracao)

    def __str__(self):
        return self.name