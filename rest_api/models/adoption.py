from __future__ import unicode_literals

from django.db import models

from rest_api.managers.adoption import AdoptionRequestManager
from rest_api.models.profile import Profile
from rest_api.models.animals import Animal

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

STARTED = 'STA'
WAIT_LIST = 'WAL'
ACCEPTED = 'ACC'
REJECTED = 'REJ'
ON_HOLD = 'ONH'
ADOPTED = 'ADO'

TYPES_OF_REQUEST_CHOICES = [
    (STARTED, 'Comenzo'),
    (WAIT_LIST, 'En espera'),
    (ACCEPTED, 'Aceptado'),
    (REJECTED, 'Rechazado'),
    (ON_HOLD, 'En revisión'),
    (ADOPTED, 'Adoptado'),

]


class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal,
                               related_name='adoption_requests_for_animal',
                               on_delete=models.CASCADE, blank=True, null=True, verbose_name='Animal')

    potencial_adopter = models.ForeignKey(Profile,
                                          related_name='adopter_requests',
                                          on_delete=models.CASCADE, blank=True, null=True, verbose_name='Profile')

    status = models.CharField(
        max_length=3,
        choices=TYPES_OF_REQUEST_CHOICES,
        default=STARTED,
        verbose_name='Tipo de Perfil'
    )
    objects = AdoptionRequestManager()

    class Meta:
        verbose_name_plural = "Solicitud de adopción de animales"