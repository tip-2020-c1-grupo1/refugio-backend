# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.models import User     # where User lives
import os                                      # env var access
from django.contrib.auth.management import create_permissions

from rest_api.models.colaboration import Colaboration


def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def forwards_func(apps, schema_editor):
    # build the user you now have access to via Django magic
    dog_short = "150 kg de alimento balanceado para perros"
    dog_long = "150 kg de alimento balanceado para perros, algunos tienen estomago sensible"

    cat_short = "Translado a Rosario para gatos"
    cat_long = "Se necesita translado para llevar desde CABA a 20 siameses a la sede del Refugio de Rosario"

    Colaboration.objects.get_or_create(name='Alimento para perros', short_description=dog_short, description=dog_long)
    Colaboration.objects.get_or_create(name='Translado de gatos', short_description=cat_short, description=cat_long)


def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass


class Migration(migrations.Migration):
    dependencies = [('rest_api', '0003_create_animal_specie')]
    operations = [
        migrations.RunPython(migrate_permissions, reverse_func),
        migrations.RunPython(forwards_func, reverse_func),
    ]