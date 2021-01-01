from .common import *
from config.logger import LOGGING


# Application definition

if HTML_MINIFY_ENABLED:
    MIDDLEWARE = [
        'apps.core.middleware.HTMLMinifyMiddleware',
    ] + MIDDLEWARE


if LOGIN_CHECK_ENABLED:
    MIDDLEWARE += [
        'apps.core.middleware.LoginCheckMiddleware',
    ]


MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
] + MIDDLEWARE


if REDIS_CACHE_ENABLED:
    # Application definition

    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',
    ] + MIDDLEWARE

    MIDDLEWARE += [
        'django.middleware.cache.FetchFromCacheMiddleware',
    ]


    # Cache

    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://redis:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    }

    CACHE_MIDDLEWARE_ALIAS = 'default'
    CACHE_MIDDLEWARE_KEY_PREFIX = ''
    CACHE_MIDDLEWARE_SECONDS = 600


if AWS_MEDIA_STORAGE:
    # Application definition

    INSTALLED_APPS += [
        'storages',
    ]


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.0/howto/static-files/

    DEFAULT_FILE_STORAGE = 'config.custom_storages.PublicMediaStorage'

    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = 'public-read'

    MEDIA_URL = '{}/{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_STORAGE_BUCKET_NAME, AWS_S3_MEDIA_ROOT)
    MEDIA_ROOT = MEDIA_URL