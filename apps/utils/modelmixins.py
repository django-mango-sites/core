import uuid
from django.template.defaultfilters import striptags, truncatewords
from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from apps.utils.helpers import get_upload_path, get_resize_image_or_none


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UuidMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class TitleMixin(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        abstract = True


class TitleSlugMixin(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class PageDescriptionMixin(models.Model):
    page_description = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        abstract = True


class PostMixin(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    body = models.TextField(blank=True, null=True)
    excerpt_short = models.TextField(blank=True, null=True)
    excerpt_long = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if self.body:
            body_raw = striptags(self.body)

            if not self.excerpt_short:
                self.excerpt_short = truncatewords(body_raw, 20)

            if not self.excerpt_long:
                self.excerpt_long = truncatewords(body_raw, 40)

        super().save(*args, **kwargs)


class ImageMixin(models.Model):
    image = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    image_xs = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    image_sm = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    image_md = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    image_lg = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    image_xl = models.ImageField(upload_to=get_upload_path, max_length=255, blank=True, null=True)
    alt = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if self.image:
            self.image_xs = get_resize_image_or_none(self.image, size=(160, 120), prefix='xs-', format='jpeg')
            self.image_sm = get_resize_image_or_none(self.image, size=(480, 360), prefix='sm-', format='jpeg')
            self.image_md = get_resize_image_or_none(self.image, size=(800, 600), prefix='md-', format='jpeg')
            self.image_lg = get_resize_image_or_none(self.image, size=(1280, 960), prefix='lg-', format='jpeg')
            self.image_xl = get_resize_image_or_none(self.image, size=(1920, 1440), prefix='xl-', format='jpeg')

        else:
            self.image_xs, self.image_sm, self.image_md, self.image_lg, self.image_xl = None, None, None, None, None

        super().save(*args, **kwargs)