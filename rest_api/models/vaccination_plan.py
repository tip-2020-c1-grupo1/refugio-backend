from __future__ import unicode_literals
from django.db import models
from rest_api.models.animals import Animal


class VaccinationPlan(models.Model):
    animal = models.OneToOneField(Animal,
                                  related_name='vaccination_plan_animals',
                                  on_delete=models.CASCADE, blank=True, null=True, verbose_name='Animal')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')

    def animal_asociado(self):
        return str(self.animal.pk) + ' - ' + self.animal.name

    class Meta:
        verbose_name_plural = "Plan vacunatorio "
        verbose_name = "Planes vacunatorios"