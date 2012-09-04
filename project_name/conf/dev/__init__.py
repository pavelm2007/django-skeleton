from {{ project_name }}.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
             'default': {
                         'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': os.path.join(ASSET_DIR, 'dev.db'),
                         }
             }

ROOT_URLCONF = '{{ project_name }}.conf.dev.urls'

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WSGI_APPLICATION = '{{ project_name }}.wsgi.dev.application'
