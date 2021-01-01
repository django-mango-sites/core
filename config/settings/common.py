import os
import json


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', False) == 'True'

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1').split(',')

SECURE_SSL_REDIRECT = os.getenv('DJANGO_SECURE_SSL_REDIRECT', False) == 'True'

if os.getenv('DJANGO_SECURE_PROXY_SSL_HEADER_CHECK', False) == 'True':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',

    'solo',

    'apps.core',
]

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/account/portal/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.core.context_processors.core',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

X_FRAME_OPTIONS = 'SAMEORIGIN'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(
            os.getenv('DATABASE_ENGINE')
        ),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USERNAME'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
        'OPTIONS': json.loads(
            os.getenv('DATABASE_OPTIONS', '{}')
        ),
    }
}


# Cache

REDIS_CACHE_ENABLED = os.getenv('DJANGO_REDIS_CACHE_ENABLED', True) == 'True'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Mail

EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST')
EMAIL_PORT = os.getenv('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('DJANGO_EMAIL_USE_TLS', True) == 'True'
EMAIL_USE_SSL = os.getenv('DJANGO_EMAIL_USE_SSL', False) == 'True'
ADMIN_EMAIL = os.getenv('DJANGO_ADMIN_EMAIL')


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AWS_MEDIA_STORAGE = os.getenv('DJANGO_AWS_MEDIA_STORAGE', False) == 'True'

AWS_S3_MEDIA_ROOT = 'media'

AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')

AWS_S3_REGION_NAME = os.getenv('DJANGO_AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_S3_DOMAIN_NAME = os.getenv('DJANGO_AWS_S3_DOMAIN_NAME')
AWS_S3_ENDPOINT_URL = 'https://{}.{}.{}'.format(AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_S3_DOMAIN_NAME)


# Other

MAX_UPLOAD_SIZE = int(os.getenv('DJANGO_MAX_UPLOAD_SIZE', default=4 * 1024 * 1024))
LOGIN_CHECK_ENABLED = os.getenv('DJANGO_LOGIN_CHECK_ENABLED', False) == 'True'
HTML_MINIFY_ENABLED = os.getenv('DJANGO_HTML_MINIFY_ENABLED', False) == 'True'