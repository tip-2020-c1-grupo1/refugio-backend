# Generated by Django 2.2.12 on 2020-07-05 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0006_auto_20200705_0337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animalspecie',
            options={'verbose_name': 'Especie de Animal', 'verbose_name_plural': 'Especies de Animales'},
        ),
    ]