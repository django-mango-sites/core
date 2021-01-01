from django.utils import timezone
from django.db import models
from solo.models import SingletonModel
from apps.utils.modelmixins import OrderMixin, TitleSlugMixin
from apps.utils.helpers import get_upload_path


class IntroMixin(SingletonModel, models.Model):
    LAYOUT_CHOICES = (
        ('body_left', 'body_left'),
        ('body_right', 'body_right'),
        ('body_full', 'body_full')
    )

    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default='body_left')
    body_animation = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class CarouselMixin(OrderMixin, models.Model):
    image = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class FocusSlideMixin(OrderMixin, models.Model):
    LAYOUT_CHOICES = (
        ('body_left', 'body_left'),
        ('body_right', 'body_right'),
        ('body_full', 'body_full')
    )

    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICES, default='body_left')
    image_animation = models.CharField(max_length=255, blank=True, null=True)
    body_animation = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class PrincipleMixin(OrderMixin, models.Model):
    icon_class = models.CharField(max_length=255, blank=True, null=True)
    principle = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class FaqMixin(OrderMixin, models.Model):
    featured = models.BooleanField(default=False)
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class DocumentMixin(TitleSlugMixin, models.Model):
    datetime = models.DateTimeField(default=timezone.now, blank=False, null=False)
    body = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
