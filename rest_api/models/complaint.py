from __future__ import unicode_literals

from django.db import models
from rest_api.models.profile import Profile

import logging
logger = logging.getLogger(__name__)

AVAILABLE = 'Disponible'


class Complaint(models.Model):
    """This class represents the Complaint model."""
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    status_request = models.CharField(
        max_length=30,
        default=AVAILABLE,
        verbose_name='Estado de colaboración'
    )
    complainer = models.ForeignKey(
        Profile,
        related_name='complaints_of_user',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Denunciante')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Denuncia"
        verbose_name = "Denuncias"