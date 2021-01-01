import os
import logging
from .settings.common import BASE_DIR
from .settings.common import DEBUG


log = logging.getLogger(__name__)

if DEBUG:
    min_level = 'DEBUG'
else:
    min_level = 'INFO'

min_django_level = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # keep Django's default loggers
    'formatters': {
        # see full list of attributes here:
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'timestampthread': {
            'format': "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(name)-20.20s]  %(message)s",
        },
    },
    'handlers': {
        'logfile': {
            'level': min_level,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'maxBytes': 50 * 10**6,
            'backupCount': 3,
            'formatter': 'timestampthread'
        },
        'console': {
            'level': min_level,
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile', 'console'],
            'level': min_django_level,
            'propagate': False,
        },
        '': {
            'handlers': ['logfile', 'console'],
            'level': min_level,
        },
    },
}