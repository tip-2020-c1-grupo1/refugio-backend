from __future__ import unicode_literals

from django.db import models
from rest_api.managers.animals import AnimalManager
from rest_api.models.profile import Profile


class Animal(models.Model):
    """This class represents the Animals model."""
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Nombre')
    species = models.CharField(max_length=255, blank=False, verbose_name='Especie')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    race = models.TextField(blank=True, null=True, verbose_name='Raza')
    gender = models.CharField(max_length=255, blank=False, null=True, verbose_name='Genero')
    owner = models.ForeignKey(
        Profile,
        related_name='animals',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Dueño')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = AnimalManager()

    class Meta:
        verbose_name_plural = "Animales"


class ImageAnimal(models.Model):
    animal = models.ForeignKey(Animal,
                               related_name='images',
                               on_delete=models.CASCADE, blank=True, null=True, verbose_name='Animal')
    image = models.ImageField(blank=True, null=True, verbose_name='Imagen')

    class Meta:
        verbose_name_plural = "Imagenes de animales"
