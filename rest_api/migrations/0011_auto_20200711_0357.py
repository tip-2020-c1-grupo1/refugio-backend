# Generated by Django 2.2.12 on 2020-07-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0010_auto_20200707_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionrequest',
            name='status',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Solicitado', 'Solicitado'), ('Rechazado', 'Rechazado'), ('Adoptado', 'Adoptado'), ('Eliminado', 'Eliminado')], default='Disponible', max_length=30, verbose_name='Estado de petición'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status_request',
            field=models.CharField(default='Disponible', max_length=30, verbose_name='Estado de denuncia'),
        ),
    ]