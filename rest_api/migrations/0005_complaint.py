# Generated by Django 2.2.12 on 2020-06-05 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20200604_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('status_request', models.CharField(default='Disponible', max_length=30, verbose_name='Estado de colaboración')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('complainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complaints_of_user', to='rest_api.Profile', verbose_name='Denunciante')),
            ],
            options={
                'verbose_name': 'Denuncias',
                'verbose_name_plural': 'Denuncia',
            },
        ),
    ]