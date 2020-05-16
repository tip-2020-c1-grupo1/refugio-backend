from __future__ import unicode_literals

from django.db import models

from rest_api.managers.adoption import AdoptionRequestManager
from rest_api.models.profile import Profile
from rest_api.models.animals import Animal

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

AVAILABLE = 'Disponible'
REQUESTED = 'Solicitado'
WAIT_LIST = 'En espera'
ACCEPTED = 'Aceptado'
REJECTED = 'Rechazado'
ON_HOLD = 'En revisión'
ADOPTED = 'Adoptado'

TYPES_OF_REQUEST_CHOICES = [
    (AVAILABLE, 'Disponible'),
    (REQUESTED, 'Solicitado'),
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
        max_length=30,
        choices=TYPES_OF_REQUEST_CHOICES,
        default=AVAILABLE,
        verbose_name='Estado de petición'
    )
    objects = AdoptionRequestManager()

    def animal_solicitado(self):
        animal = self.animal
        return animal.name + ' - ' + animal.species + ' - ' + animal.race

    def potencial_adoptante(self):
        profile = self.potencial_adopter.user
        return profile.username + ' - ' + profile.email

    class Meta:
        verbose_name_plural = "Solicitudes de adopción"
        verbose_name = "Solicitud de adopción"