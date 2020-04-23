from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.core.cache import cache

REDIRECTS_KEY = "animals.all"

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# This receiver handles token creation when a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Animal(models.Model):
    """This class represents the Animals model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    species = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True, null=True) 
    owner = models.ForeignKey(
        'auth.User',
        related_name='animals',
        on_delete=models.CASCADE, blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    

class ImageAnimal(models.Model):
    animal = models.ForeignKey(Animal,
        related_name='images',
        on_delete=models.CASCADE, blank=True,null=True)
    image = models.ImageField(blank=True, null=True)

@receiver(post_save, sender=Animal)
def create_animal(sender, instance, created, **kwargs):
    print('Preparing to save into cache')
    print(cache.get(REDIRECTS_KEY))