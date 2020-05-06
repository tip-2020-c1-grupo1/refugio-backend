# Generated by Django 2.2.12 on 2020-05-06 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
                ('species', models.CharField(max_length=255, verbose_name='Especie')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('race', models.TextField(blank=True, null=True, verbose_name='Raza')),
                ('status_request', models.CharField(default='AVA', max_length=3, verbose_name='Estado de adopción')),
                ('gender', models.CharField(max_length=255, null=True, verbose_name='Genero')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animales',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('image_url', models.TextField(blank=True, max_length=800, null=True, verbose_name='Url de imagen')),
                ('google_id', models.CharField(blank=True, max_length=80, null=True, verbose_name='Id de Google')),
                ('type_of_profile', models.CharField(choices=[('ADO', 'Adoptante'), ('REF', 'Refugio'), ('ADM', 'Admin')], default='ADO', max_length=3, verbose_name='Tipo de Perfil')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Id de Google')),
            ],
            options={
                'verbose_name_plural': 'Perfiles',
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('animal', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='rest_api.Animal', verbose_name='Animal')),
            ],
            options={
                'verbose_name': 'Linea del tiempo para animal',
                'verbose_name_plural': 'Lineas del tiempo de animales',
            },
        ),
        migrations.CreateModel(
            name='RefugioEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('metadata', models.TextField(blank=True, null=True, verbose_name='Metadata')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refugio_events_reported', to='rest_api.Profile', verbose_name='Personal del refugio')),
                ('timeline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refugio_events', to='rest_api.Timeline', verbose_name='Linea del tiempo')),
            ],
            options={
                'verbose_name': 'Evento del refugio',
                'verbose_name_plural': 'Eventos del refugio',
            },
        ),
        migrations.CreateModel(
            name='ImageAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rest_api.Animal', verbose_name='Animal')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Imagenes de animales',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='rest_api.Profile', verbose_name='Dueño'),
        ),
        migrations.CreateModel(
            name='AdoptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AVA', 'Disponible'), ('STA', 'Comenzo'), ('WAL', 'En espera'), ('ACC', 'Aceptado'), ('REJ', 'Rechazado'), ('ONH', 'En revisión'), ('ADO', 'Adoptado')], default='AVA', max_length=3, verbose_name='Estado de petición')),
                ('animal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adoption_requests_for_animal', to='rest_api.Animal', verbose_name='Animal')),
                ('potencial_adopter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adopter_requests', to='rest_api.Profile', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Solicitud de adopción',
                'verbose_name_plural': 'Solicitudes de adopción',
            },
        ),
    ]
