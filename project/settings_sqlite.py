from project.base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!zxmc^48#eli@!494w9^#56#nf*xp7s&#zu+n)82z&yxsnwnu#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']


WSGI_APPLICATION = 'project.wsgi_sqlite.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
