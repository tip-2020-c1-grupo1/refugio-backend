# Generated by Django 2.2.12 on 2020-07-07 01:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0009_animal_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripcion detallada'),
        ),
    ]