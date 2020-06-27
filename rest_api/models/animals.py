from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_api.managers.animals import AnimalManager
from rest_api.models.profile import Profile
from ckeditor.fields import RichTextField
from markdownx.models import MarkdownxField
import logging

# Get an instance of a logger
from rest_api.services.timeline import TimelineService

logger = logging.getLogger(__name__)

AVAILABLE = 'Disponible'


class AnimalSpecie(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Especie')
    default_vaccination_plan = RichTextField(verbose_name='Plan vacunatorio por default')

    def __str__(self):
        return self.name


class Animal(models.Model):
    """This class represents the Animals model."""
    name = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Nombre')
    species = models.ForeignKey(
        AnimalSpecie,
        related_name='animal_specie',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Especie')
    description = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    race = models.CharField(max_length=255, blank=True, null=True, verbose_name='Raza')
    status_request = models.CharField(
        max_length=30,
        default=AVAILABLE,
        verbose_name='Estado de adopción'
    )
    gender = models.CharField(max_length=255, blank=False, null=True, verbose_name='Genero')
    owner = models.ForeignKey(
        Profile,
        related_name='animals',
        on_delete=models.CASCADE, blank=True, null=True, verbose_name='Dueño')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    vaccination_plan = RichTextField(verbose_name='Plan vacunatorio')
    #models.TextField(blank=True, null=True, verbose_name='Plan vacunatorio')
    objects = AnimalManager()

    def especie_animal(self):
        return self.species.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Animales"
        verbose_name = "Animal"


class ImageAnimal(models.Model):
    animal = models.ForeignKey(Animal,
                               related_name='images',
                               on_delete=models.CASCADE, blank=True, null=True, verbose_name='Animal')
    image = models.ImageField(blank=True, null=True, verbose_name='Imagen')

    class Meta:
        verbose_name_plural = "Imagenes de animales"
        verbose_name = "Animal"


@receiver(post_save, sender=Animal)
def create_animal(sender, instance, created, **kwargs):
    logger.info(instance.__dict__)
    print(instance.__dict__)
    if created:
        TimelineService.create_initial_timeline(animal=instance)
        if instance.species is not None:
            instance.vaccination_plan = instance.species.default_vaccination_plan
            instance.save()
        else:
            instance.vaccination_plan = 'Te vino vacio'
            instance.save()