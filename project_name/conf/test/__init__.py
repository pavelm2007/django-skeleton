from {{ project_name }}.settings import *

DEBUG = False
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
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

ROOT_URLCONF = '{{ project_name }}.conf.test.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.test.application'
