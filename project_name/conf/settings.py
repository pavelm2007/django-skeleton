from {{ project_name }}.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
          ('You', 'you@your.email'),
)
MANAGERS = ADMINS

DATABASES = {
             'default': {
                         'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': os.path.join(ASSET_DIR, 'dev.db'),
                         }
             }

INSTALLED_APPS += (
    'django_extensions',
)

ROOT_URLCONF = '{{ project_name }}.conf.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'
