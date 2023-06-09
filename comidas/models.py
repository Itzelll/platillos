from django.db import models
from django.conf import settings

# Create your models here.
class Comida(models.Model):
    nombre = models.TextField(default='', blank=False)
    tipo_platillo = models.TextField(default='', blank=False)
    calorias = models.FloatField(default=0, blank=False)
    proteinas = models.FloatField(default=0, blank=False)
    pais_origen = models.TextField(default='', blank=False)
    ingredientes = models.TextField(default='', blank=False)
    saludable = models.TextField(default='Si', blank=False)
    tiempo_coccion = models.IntegerField(default=0, blank=False)
    dificultad_preparacion = models.PositiveSmallIntegerField(default=1, blank=False)
    utensilios_requeridos = models.TextField(default='', blank=False)
    
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    platillo = models.ForeignKey('comidas.Comida', related_name='platillos', on_delete=models.CASCADE)
