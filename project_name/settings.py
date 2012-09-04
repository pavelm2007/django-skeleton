# Import global settings, makes it easier to extend settings
from django.conf.global_settings import *

#===============================================================================
# General project settings
#===============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
TIME_ZONE = 'US/Eastern'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', 'English'),
)

SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = (
    # General Includes
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Project specific includes
    # '{{ project_name }}.apps.',
    # 'south',
)

#===============================================================================
# Project location configuration
#===============================================================================
import os
import {{ project_name }} as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
VAR_ROOT = os.path.join(PROJECT_DIR, 'conf', 'local')

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = '{{ project_name }}.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/site_media/static/'
MEDIA_URL = '/site_media/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media', 'media')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

#==============================================================================
# Templates
#==============================================================================

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================
