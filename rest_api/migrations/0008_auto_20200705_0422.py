# Generated by Django 2.2.12 on 2020-07-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0007_auto_20200705_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboration',
            name='status_request',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Reservado', 'Reservado'), ('Confirmado', 'Confirmado')], default='Disponible', max_length=30, verbose_name='Estado de colaboración'),
        ),
        migrations.AlterField(
            model_name='colaborationcolaborators',
            name='status_request',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Reservado', 'Reservado'), ('Confirmado', 'Confirmado')], default='Reservado', max_length=30, verbose_name='Estado de colaboración'),
        ),
    ]
