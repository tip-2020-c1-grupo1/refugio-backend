from __future__ import unicode_literals

from django.db import models
from rest_api.models.profile import Profile
from ckeditor.fields import RichTextField

import logging
logger = logging.getLogger(__name__)

AVAILABLE = 'Disponible'
REJECTED = 'Rechazado'
ACEPTADO = 'Aceptado'

TYPES_OF_REQUEST_CHOICES = [
    (AVAILABLE, 'Disponible'),
    (REJECTED, 'Rechazado'),
    (ACEPTADO, 'Aceptado'),
]


class Complaint(models.Model):
    """This class represents the Complaint model."""
    description = RichTextField(blank=True, null=True, verbose_name='Descripción')
    status_request = models.CharField(
        max_length=30,
        choices=TYPES_OF_REQUEST_CHOICES,
        default=AVAILABLE,
        verbose_name='Estado de denuncia'
    )
    complainer = models.ForeignKey(
        Profile,
        related_name='complaints_of_user',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Denunciante')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    class Meta:
        verbose_name_plural = "Denuncia"
        verbose_name = "Denuncias"