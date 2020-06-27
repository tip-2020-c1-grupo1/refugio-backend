from project.base_settings import *
import os
import django_heroku
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!zxmc^48#eli@!494w9^#56#nf*xp7s&#zu+n)82z&yxsnwnu#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'project.wsgi_postgres.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Ejemplo_DB',
        'USER': 'Ejemplo_Usuario',
        'PASSWORD': 'password_usuario',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""
# DOCKERIZED
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

DATABASES = {
    'default': dj_database_url.config()
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


"""
REQUERED FOR https://vxlabs.com/2015/12/08/gunicorn-as-your-django-development-server/
SETUP GUNICORN + DJ-STATIC

ALSO CHECK: https://github.com/heroku-python/dj-static

TODO: WHITENOISE INTEGRATION
"""
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SUPER_USER = {
    'username': 'admin',
    'email':'admin@admin.com',
    'password':'admin',
}

MP_URLS = {
        'success': 'http://refugio-frontend.herokuapp.com/donacion',
        'pending': 'http://refugio-frontend.herokuapp.com/donacion',
        'failure': 'http://refugio-frontend.herokuapp.com/donacion'
}

django_heroku.settings(locals())
