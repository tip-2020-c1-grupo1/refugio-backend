from __future__ import unicode_literals
from django.db import models
from rest_api.models.animals import Animal


class Timeline(models.Model):
    animal = models.OneToOneField(Animal,
                                  related_name='animals',
                                  on_delete=models.CASCADE, blank=True, null=True, verbose_name='Animal')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')

    class Meta:
        verbose_name_plural = "Lineas del tiempo de animales"
        verbose_name = "Linea del tiempo para animal"