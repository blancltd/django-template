# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from importlib import import_module
import os

from .base import *  # NOQA @UnusedWildImport


DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', '{{ project_name }}_django'),
        'USER': '',
        'PASSWORD': '',
        'PORT': '',
    },
}

INTERNAL_IPS = (
    '127.0.0.1',
)

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]


# Add flat theme if module is installed.
try:
    import_module('flat')
except ImportError:
    pass
else:
    INSTALLED_APPS.insert(0, 'flat')


MIDDLEWARE_CLASSES = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE_CLASSES


COVERAGE_EXCLUDES_FOLDERS = ['/var/envs/{{ project_name }}/lib/python2']


SECRET_KEY = '{{ project_name }}'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
