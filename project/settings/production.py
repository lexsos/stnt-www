from .common import *


DEBUG = False
for tmpl in TEMPLATES:
    tmpl['OPTIONS']['debug'] = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stnt',
        'USER': 'stnt',
        'HOST': 'localhost',
        'PORT': '',
        'PASSWORD': '',
    }
}

INSTALLED_APPS += (
    'gunicorn',
)

USE_X_FORWARDED_HOST = True

try:
    from .secret import SECRET_KEY
except:
    print 'Need secret.py file with SECRET_KEY'
