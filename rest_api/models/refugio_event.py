from __future__ import unicode_literals

from django.db import models
from rest_api.models.profile import Profile
from rest_api.models.timeline import Timeline


class RefugioEvent(models.Model):
    """This class represents the RefugioEvent model."""
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    timeline = models.ForeignKey(
        Timeline,
        related_name='refugio_events',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Linea del tiempo')
    reported_by = models.ForeignKey(
        Profile,
        related_name='refugio_events_reported',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Personal del refugio')
    metadata = models.TextField(blank=True, null=True, verbose_name='Metadata')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Eventos del refugio"
        verbose_name = "Evento del refugio"
