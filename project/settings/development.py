import os

from .common import *


DEBUG = True
for tmpl in TEMPLATES:
    tmpl['OPTIONS']['debug'] = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = INTERNAL_IPS

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

SECRET_KEY = '_6_8%3_#i+di=a5z0gdh_eke%u^oa=f=#ik@px^h&9yp1xqur1'
