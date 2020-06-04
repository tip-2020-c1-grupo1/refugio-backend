from __future__ import unicode_literals

from django.db import models
from rest_api.models.profile import Profile

import logging
logger = logging.getLogger(__name__)

AVAILABLE = 'Disponible'


class Colaboration(models.Model):
    """This class represents the Colaboration model."""
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Nombre')
    short_description = models.CharField(max_length=255, blank=False, verbose_name='Descripcion corta')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    status_request = models.CharField(
        max_length=30,
        default=AVAILABLE,
        verbose_name='Estado de colaboración'
    )
    colaborator = models.ForeignKey(
        Profile,
        related_name='colaborations_of_user',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Colaborador')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Colaboraciones"
        verbose_name = "Colaboración"