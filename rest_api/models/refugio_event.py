from __future__ import unicode_literals

from django.db import models
from rest_api.models.profile import Profile
from rest_api.models.timeline import Timeline


class RefugioEvent(models.Model):
    """This class represents the RefugioEvent model."""
    title = models.CharField(max_length=80, verbose_name='Titulo')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    timeline = models.ForeignKey(
        Timeline,
        related_name='refugio_events',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Linea del tiempo')
    reported_by = models.ForeignKey(
        Profile,
        related_name='refugio_events_reported',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Personal del refugio')
    metadata = models.TextField(blank=True, null=True, verbose_name='Metadata')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Fecha modificación')

    def cambio_realizado_por(self):
        return self.reported_by.user.email if self.reported_by else ''

    class Meta:
        verbose_name_plural = "Eventos del refugio"
        verbose_name = "Evento del refugio"
