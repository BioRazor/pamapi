from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Bussines_unit(TimeStampedModel):
    """
        Class for the Bussines Units of the Company, like
        conssesionaries or departaments of the company itself.
    """

    name = models.CharField(max_length=50, verbose_name='Nombre')
    

    class Meta:
        verbose_name = ("Unidad de Negocio")
        verbose_name_plural = ("Unidades de Negocios")

    def __str__(self):
        return self.name