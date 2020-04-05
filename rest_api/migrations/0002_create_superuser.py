# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User     # where User lives
import os                                      # env var access

def forwards_func(apps, schema_editor):
  # build the user you now have access to via Django magic
    if not User.objects.filter(username='admin').exists() : 
      User.objects.create_superuser('admin', password='superuser123', email='admin@admin.com')
    else:
      print('Superuser already created')

def reverse_func(apps, schema_editor):
    # destroy what forward_func builds
    pass

class Migration(migrations.Migration):
    dependencies = [ ('rest_api', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]