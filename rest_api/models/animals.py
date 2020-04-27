from __future__ import unicode_literals

from django.db import models
from rest_api.managers.animals import AnimalManager
from rest_api.models.profile import Profile


class Animal(models.Model):
    """This class represents the Animals model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    species = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=False, null=True)
    owner = models.ForeignKey(
        Profile,
        related_name='animals',
        on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = AnimalManager()


class ImageAnimal(models.Model):
    animal = models.ForeignKey(Animal,
                               related_name='images',
                               on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
