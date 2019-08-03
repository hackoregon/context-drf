import os
import dj_database_url

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']

# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:password@host.docker.internal:5000/scooters',
        conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
    )
}

INSTALLED_APPS = (
    'test_project.scooters',

    'context',

    'debug_toolbar',
    'django_extensions',
    'rest_framework',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
)

STATIC_URL = '/static/'
SECRET_KEY = 'foo'

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

ROOT_URLCONF = 'example.urls'

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]