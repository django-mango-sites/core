from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = settings.AWS_S3_MEDIA_ROOT


class PrivateMediaStorage(S3Boto3Storage):
    default_acl = 'private'
    location = settings.AWS_S3_MEDIA_ROOT