from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from apps.utils.modelmixins import TimestampMixin, TitleSlugMixin, OrderMixin


def site_config_post_save(sender, instance, created, **kwargs):

    if created:
        related_models = [
            NavigationLink,
            SocialLink,
            ContactDetail,
            AboutDetail,
            Disqus,
        ]

        for related_model in related_models:
            related_model.objects.create(site_config=instance)


class SiteConfiguration(TimestampMixin, models.Model):
    site_name = models.CharField(max_length=255, default='Site Name')
    site_url = models.URLField(blank=True)
    site_description = models.CharField(max_length=160, blank=True, null=True)
    maintenance_mode = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configurations"

    def __str__(self):
        return self.site_name


post_save.connect(site_config_post_save, sender=SiteConfiguration, dispatch_uid='site_config_post_save')


class NavigationLink(TimestampMixin, OrderMixin, TitleSlugMixin, models.Model):
    site_config = models.ForeignKey(SiteConfiguration, related_name='navigation_link', verbose_name=_('Config'),
                                    on_delete=models.SET_NULL, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child', blank=True, null=True)

    featured = models.BooleanField(default=False)
    target = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Navigation Link"
        verbose_name_plural = "Navigation Links"
        ordering = ['order']

    def __str__(self):
        return self.site_config.site_name


class SocialLink(TimestampMixin, OrderMixin, TitleSlugMixin, models.Model):
    site_config = models.ForeignKey(SiteConfiguration, related_name='social_link', verbose_name=_('Config'),
                                    on_delete=models.SET_NULL, blank=True, null=True)

    icon_class = models.CharField(max_length=255, blank=True, null=True)
    social_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering = ['order']

    def __str__(self):
        return self.site_config.site_name


class ContactDetail(TimestampMixin, models.Model):
    site_config = models.OneToOneField(SiteConfiguration, related_name='contact_detail', verbose_name=_('Config'),
                                       on_delete=models.SET_NULL, blank=True, null=True)

    email = models.CharField(max_length=70, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Contact Detail"
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return self.site_config.site_name


class AboutDetail(TimestampMixin, models.Model):
    site_config = models.OneToOneField(SiteConfiguration, related_name='about_detail', verbose_name=_('Config'),
                                       on_delete=models.SET_NULL, blank=True, null=True)

    summary = models.TextField(blank=True)

    class Meta:
        verbose_name = "About Detail"
        verbose_name_plural = "About Details"

    def __str__(self):
        return self.site_config.site_name


class Disqus(TimestampMixin, models.Model):
    site_config = models.OneToOneField(SiteConfiguration, related_name='disqus', verbose_name=_('Config'),
                                       on_delete=models.SET_NULL, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    disqus_url = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Disqus"
        verbose_name_plural = "Disqus"

    def __str__(self):
        return self.site_config.site_name