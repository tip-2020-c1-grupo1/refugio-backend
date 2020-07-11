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
REJECTED = 'Rechazado'
ADOPTED = 'Adoptado'
REMOVED = 'Eliminado'

TYPES_OF_REQUEST_CHOICES = [
    (AVAILABLE, 'Disponible'),
    (REQUESTED, 'Solicitado'),
    (REJECTED, 'Rechazado'),
    (ADOPTED, 'Adoptado'),
    (REMOVED, 'Eliminado'),
]


class AdoptionRequest(models.Model):
    animal = models.ForeignKey(Animal,
                               related_name='adoption_requests_for_animal',
                               on_delete=models.CASCADE, blank=True, null=True, verbose_name='Animal')

    potencial_adopter = models.ForeignKey(Profile,
                                          related_name='adopter_requests',
                                          on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario adoptante')

    status = models.CharField(
        max_length=30,
        choices=TYPES_OF_REQUEST_CHOICES,
        default=AVAILABLE,
        verbose_name='Estado de petición'
    )
    objects = AdoptionRequestManager()

    def __str__(self):
        return 'Solicitud por ' + self.animal.name + " por: " + self.potencial_adopter.user.username

    def animal_solicitado(self):
        animal = self.animal
        return animal.name + ' - ' + animal.species.name + ' - ' + animal.race

    def potencial_adoptante(self):
        if self.potencial_adopter is None:
            return ''
        profile = self.potencial_adopter.user
        return profile.username + ' - ' + profile.email

    class Meta:
        verbose_name_plural = "Solicitudes de adopción"
        verbose_name = "Solicitud de adopción"