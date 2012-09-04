from {{ project_name }}.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
          ('You', 'you@email.com'),
)
MANAGERS = ADMINS

DATABASES = {
             'default': {
                         'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': os.path.join(VAR_ROOT, 'dev.db'),
                         }
             }

ROOT_URLCONF = '{{ project_name }}.conf.local.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.local.application'
