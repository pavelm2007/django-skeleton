from {{ project_name }}.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ project_name }}',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

INSTALLED_APPS += (
    'south',
)

ROOT_URLCONF = '{{ project_name }}.conf.production.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'
