from {{ project_name }}.settings import *

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

WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'
