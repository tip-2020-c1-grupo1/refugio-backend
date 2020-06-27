from __future__ import unicode_literals
from django.db import models
from rest_api.models.profile import Profile

import logging

logger = logging.getLogger(__name__)


class Colaboration(models.Model):
    AVAILABLE = 'Disponible'
    RESERVED = 'Reservado'
    CONFIRMED = 'Confirmado'
    """This class represents the Colaboration model."""
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Nombre')
    short_description = models.CharField(max_length=255, blank=False, verbose_name='Descripcion corta')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    status_request = models.CharField(
        max_length=30,
        default=AVAILABLE,
        verbose_name='Estado de colaboración'
    )
    satisfied = models.BooleanField(default=False)
    required_colaborators = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Colaboraciones"
        verbose_name = "Colaboración"

    @property
    def colaboration_colab_users(self):
        self.colaboration_colab.all()


class ColaborationColaborators(models.Model):
    colaborator = models.ForeignKey(Profile,
                                    related_name='colaboration_users',
                                    on_delete=models.CASCADE, blank=True, null=True, verbose_name='Colaborators')
    colaboration = models.ForeignKey(Colaboration, related_name='colaboration_colab',
                                     on_delete=models.CASCADE, blank=True, null=True, verbose_name='Colaboration')
    status_request = models.CharField(
        max_length=30,
        default=Colaboration.RESERVED,
        verbose_name='Estado de colaboración'
    )

    class Meta:
        verbose_name_plural = "Colaboraciones de Usuarios"
        verbose_name = "Colaboración de Usuario"
