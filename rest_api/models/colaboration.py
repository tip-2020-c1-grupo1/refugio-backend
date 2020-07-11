from __future__ import unicode_literals
from django.db import models
from rest_api.models.profile import Profile

import logging

logger = logging.getLogger(__name__)


AVAILABLE = 'Disponible'
RESERVED = 'Reservado'
CONFIRMED = 'Confirmado'

TYPES_OF_REQUEST_CHOICES = [
    (AVAILABLE, 'Disponible'),
    (RESERVED, 'Reservado'),
    (CONFIRMED, 'Confirmado')
]


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
        choices=TYPES_OF_REQUEST_CHOICES,
        verbose_name='Estado de colaboración'
    )
    satisfied = models.BooleanField(default=False, verbose_name='Satisfecha')
    required_colaborators = models.IntegerField(default=1, verbose_name='Colaboradores requeridos')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    date_end = models.DateTimeField(blank=True, null=True, verbose_name='Fecha fin')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    class Meta:
        verbose_name_plural = "Colaboraciones"
        verbose_name = "Colaboración"

    def __str__(self):
        return 'Colaboración ' + str(self.pk) + " : " + self.short_description

    @property
    def colaboration_colab_users(self):
        self.colaboration_colab.all()


class ColaborationColaborators(models.Model):
    colaborator = models.ForeignKey(Profile,
                                    related_name='colaboration_users',
                                    on_delete=models.CASCADE, blank=True, null=True, verbose_name='Colaboradores')
    colaboration = models.ForeignKey(Colaboration,
                                     related_name='colaboration_colab',
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True,
                                     verbose_name='Colaboración')
    status_request = models.CharField(
        max_length=30,
        default=Colaboration.RESERVED,
        choices=TYPES_OF_REQUEST_CHOICES,
        verbose_name='Estado de colaboración'
    )

    def __str__(self):
        return 'Objecto de colaboración ' + str(self.pk)

    class Meta:
        verbose_name_plural = "Colaboraciones de Usuarios"
        verbose_name = "Colaboración de Usuario"
