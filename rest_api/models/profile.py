from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Permission, User
from django.dispatch import receiver

from rest_api.managers.profile import ProfileManager

from django.db.models.signals import post_save
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

REFUGIO = 'REF'
ADMIN = 'ADM'
ADOPTER = 'ADO'
TYPES_OF_PROFILE_CHOICES = [
    (ADOPTER, 'Adoptante'),
    (REFUGIO, 'Refugio'),
    (ADMIN, 'Admin'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Usuario')
    image_url = models.TextField(max_length=800, null=True, blank=True, verbose_name='Url de imagen')
    google_id = models.CharField(max_length=80, null=True, blank=True, verbose_name='Id de Google')
    type_of_profile = models.CharField(
        max_length=3,
        choices=TYPES_OF_PROFILE_CHOICES,
        default=ADOPTER,
        verbose_name= 'Tipo de Perfil'
    )
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Id de Google')
    objects = ProfileManager()

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Perfiles"


@receiver(post_save, sender=Profile)
def create_redirect(sender, instance, created, **kwargs):
    if instance.type_of_profile == REFUGIO:
        logger.info('Preparing to save permissions for user')
        print('Preparing to save permissions for user')
        create_default_permission_for_refugio(instance.user)


def full_permission(user_from_profile, name):
    for elem in ['add_', 'change_', 'delete_', 'view_']:
        codename = elem + name
        permission = Permission.objects.get(codename=codename)
        user_from_profile.user_permissions.add(permission)


def add_change_permission(user_from_profile, name):
    for elem in ['add_', 'change_', 'view_']:
        codename = elem + name
        permission = Permission.objects.get(codename=codename)
        user_from_profile.user_permissions.add(permission)


def readonly_permission(user_from_profile, name):
    codename = 'view_' + name
    print(codename)
    permission = Permission.objects.get(codename=codename)
    user_from_profile.user_permissions.add(permission)


def create_default_permission_for_refugio(user_from_profile):
    full_permission(user_from_profile, "animal")
    full_permission(user_from_profile, "imageanimal")
    full_permission(user_from_profile, "user")
    full_permission(user_from_profile, 'profile')