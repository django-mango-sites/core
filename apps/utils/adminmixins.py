from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


class GenericAdmin(admin.ModelAdmin):

    def get_list_display(self, request):
        items = super().get_list_display(request)
        items.insert(0, 'id')

        return items


class TimeStampAdminMixin(object):
    list_display = [
        'created_at',
        'modified_at',
    ]


class UuidAdminMixin(object):
    list_display = [
        'uuid',
    ]


class OrderAdminMixin(object):
    list_display = [
        'order',
    ]


class TitleAdminMixin(object):
    list_display = [
        'title',
    ]


class TitleSlugAdminMixin(object):
    list_display = [
        'title',
        'slug',
    ]


class PageDescriptionAdminMixin(object):
    list_display = [
        'page_description',
    ]


class PostAdminMixin(SummernoteModelAdmin):
    list_display = [
        'datetime',
        'featured',
    ]

    summernote_fields = [
        'body',
    ]


class ImageAdminMixin(object):
    list_display = [
        'image',
        'alt',
    ]


class IntroAdminMixin(SummernoteModelAdmin):
    list_display = [
        'layout',
        'body_animation',
    ]

    summernote_fields = [
        'body',
    ]


class CarouselAdminMixin(SummernoteModelAdmin):
    list_display = [
        'order',
    ]

    summernote_fields = [
        'body',
    ]


class FocusSlideAdminMixin(SummernoteModelAdmin):
    list_display = [
        'order',
        'layout',
        'image_animation',
        'body_animation',
        'image',
    ]

    summernote_fields = [
        'body',
    ]


class PrincipleAdminMixin(object):
    list_display = [
        'order',
        'icon_class',
        'principle',
    ]


class FaqAdminMixin(object):
    list_display = [
        'order',
        'featured',
        'question',
    ]


class DocumentAdminMixin(SummernoteModelAdmin):
    list_display = [
        'title',
        'datetime',
    ]

    summernote_fields = [
        'body',
    ]