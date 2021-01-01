from .common import *
from config.logger import LOGGING


INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Toolbar

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}


# Mail

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
