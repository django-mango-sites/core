from django.contrib import admin
from apps.core.models import SiteConfiguration, NavigationLink, ContactDetail, AboutDetail, SocialLink, Disqus


class NavigationLinkInlineAdmin(admin.TabularInline):
    model = NavigationLink
    extra = 0

    list_display = [
        'order',
        'title',
        'featured',
        'target',
        'parent',
    ]


class SocialLinkInlineAdmin(admin.TabularInline):
    model = SocialLink
    extra = 0

    list_display = [
        'order',
        'title',
        'icon_class',
        'social_url',
    ]


class ContactDetailInlineAdmin(admin.TabularInline):
    model = ContactDetail
    extra = 0

    list_display = [
        'email',
        'address',
        'phone',
    ]


class AboutDetailInlineAdmin(admin.TabularInline):
    model = AboutDetail
    extra = 0

    list_display = [
        'summary',
    ]


class DisqusUrlInlineAdmin(admin.TabularInline):
    model = Disqus
    extra = 0

    list_display = [
        'is_active',
        'disqus_url',
    ]


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'site_name',
        'site_url',
        'maintenance_mode',
        'is_active',
        'created_at',
        'modified_at',
    ]

    list_display_links = [
        'id',
    ]

    fields = [
        'site_name',
        'site_url',
        'site_description',
        'maintenance_mode',
        'is_active',
        'created_at',
        'modified_at',
    ]

    readonly_fields = [
        'created_at',
        'modified_at',
    ]

    inlines = [
        NavigationLinkInlineAdmin,
        SocialLinkInlineAdmin,
        ContactDetailInlineAdmin,
        AboutDetailInlineAdmin,
        DisqusUrlInlineAdmin,
    ]
