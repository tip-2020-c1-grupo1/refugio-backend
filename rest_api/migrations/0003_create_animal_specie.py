# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth.models import User     # where User lives
import os                                      # env var access
from django.contrib.auth.management import create_permissions

from rest_api.models.animals import AnimalSpecie
from rest_api.services.profile import ProfileService


def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def forwards_func(apps, schema_editor):
    # build the user you now have access to via Django magic
    dog = """
    1° Semana	Es importantísima la estadía del cachorro con su madre ya que los primeros tres días recibirán el calostro que les proporcionará importante cantidad de anticuerpos para poder reaccionar ante sustancias extrañas.
Estos anticuerpos permanecerán en los cachorros, alrededor de la sexta semana de vida donde comienzan a declinar y es aquí donde se los debe vacunar por primera vez.
2° Semana	Se realiza la primera desparasitación de los cachorros, la misma debe ser en gotas y se realiza de acuerdo al peso de los mismos.
Laboratorios Over cuenta con OVERSOLE PA, un antihelmíntico de administración oral, que nos asegura en esta etapa de la vida de los cachorros la acción directa contra Ancylostomas y Áscaris
3° Semana	Se comienza a suplementar a los cachorros con papillas, en el mercado hay muy buenas formulaciones que ayudan a que este paso sea lo más natural posible para evitar accidentes dentro de la cría.
Esto es muy importante en crías numerosas, ya que obviamente existe diversidad en el tamaño como también en el comportamiento de los cachorros.
4° Semana	Se realiza la segunda desparasitación de los cachorros, esta es contra coccidios.
Son parásitos microscópicos, básicamente células simples que infectan el intestino, esto acarrea diarrea sanguinolenta con importante pérdida de líquidos, lo cual puede provocar la muerte en animales muy jóvenes.
6° Semana	Como citamos anteriormente este es el momento donde la protección de los anticuerpos maternos comienza a descender, es por esto que se aplica la primer vacuna (45 días de vida).
Es aquí donde el animal comienza a tener inmunidad activa, esta se da porque el animal comienza a fabricar sus propios anticuerpos ya sea por la vacuna o por contacto con el virus.
8° Semana	En este momento se coloca la segunda vacuna, ya que han desaparecido totalmente los anticuerpos maternos, y actúa reforzando los anticuerpos generados por la primera.
Hay que tener en cuenta que a esta edad los cachorros son retirados del criadero e ingresan a su nuevo hogar, esto trae acarreado un cuadro de estrés, que es normal, pero que afecta su inmunidad.
También se realiza una nueva desparasitación contra ancylostomas y áscaris, que son los parásitos más comunes en los cachorros de esta edad.
12° o 13° Semana	La tercera vacuna del cachorro en líneas generales se la coloca a las 12 semanas, pero esto depende del profesional actuante, ya que también se la puede colocar a las 13 ó 14 semanas
    """

    cat = """
    Semana 1	La permanencia de los cachorros junto a su madre es inminente durante los primeros tres días, ya que esa primera leche llamada calostro les proporcionará los anticuerpos necesarios, quienes actuarán como defensa frente la agresión de sustancias extrañas.
Estos anticuerpos permanecerán en los cachorros hasta la sexta semana de vida.
Semana 2	Primera dosis de antiparasitario. Se sugiere repetir el tratamiento cada 3 ó 4 meses, no obstante los análisis de materia fecal para recuento de huevos es lo recomendado antes de cualquier tratamiento.
Semana 6	En esta semana se debe inicar plan vacunal, se recomienda la aplicación de la vacuna Triple Viral (Calicivirosis felina, Panleucopenia felina y Rinotraqueitis) y la vacuna contra la Leucemia Felina.
Semana 10	Segunda dosis de las vacunas Triple Viral (Calicivirosis felina, Panleucopenia felina y Rinotraqueitis) y la vacuna contra la Leucemia Felina. Primera dosis de la vacuna Antirrábica.
Una vez al año	Refuerzo de todas las vacunas.
    """

    sloth = """
    En este momento no tenemos ninguno para un sloth
    """

    ferris = """
    En este momento no tenemos ninguno para un ferris
    """

    AnimalSpecie.objects.get_or_create(name='Perro', default_vaccination_plan=dog)
    AnimalSpecie.objects.get_or_create(name='Gato', default_vaccination_plan=cat)
    AnimalSpecie.objects.get_or_create(name='Sloth', default_vaccination_plan=sloth)
    AnimalSpecie.objects.get_or_create(name='Ferris', default_vaccination_plan=ferris)

def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass


class Migration(migrations.Migration):
    dependencies = [('rest_api', '0002_create_superuser')]
    operations = [
        migrations.RunPython(migrate_permissions, reverse_func),
        migrations.RunPython(forwards_func, reverse_func),
    ]