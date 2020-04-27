from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_api.managers.profile import ProfileManager

REFUGIO = 'REF'
ADMIN = 'ADM'
ADOPTER = 'ADO'
TYPES_OF_PROFILE_CHOICES = [
    (ADOPTER, 'Adopter'),
    (REFUGIO, 'Refugio'),
    (ADMIN, 'Admin'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    image_url = models.TextField(max_length=800, null=True, blank=True)
    google_id = models.CharField(max_length=80, null=True, blank=True)
    type_of_profile = models.CharField(
        max_length=3,
        choices=TYPES_OF_PROFILE_CHOICES,
        default=ADOPTER,
    )
    objects = ProfileManager()